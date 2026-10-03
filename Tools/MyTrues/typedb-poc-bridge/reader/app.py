from __future__ import annotations

import base64
import hashlib
import hmac
import json
import os
import re
import secrets
import time
import unicodedata
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urlencode

import httpx
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import FileResponse, JSONResponse, RedirectResponse
from pydantic import BaseModel, Field

ROOT = Path(__file__).resolve().parent
INDEX = ROOT / "index.html"

OAUTH_BASE = os.getenv("OAUTH_BASE", "https://mcp.mytrues.io").rstrip("/")
TYPEDB_URL = os.getenv(
    "TYPEDB_URL",
    "https://mytrues-tdb-e2f9605d-eastus2.eastus2.cloudapp.azure.com",
).rstrip("/")
TYPEDB_DB = os.getenv("TYPEDB_DB", "mytrues_memory_poc_v0")
TYPEDB_USERNAME = os.getenv("TYPEDB_USERNAME", "admin")
TYPEDB_PASSWORD = os.environ["TYPEDB_PASSWORD"]
SESSION_KEY = os.environ["READER_SESSION_KEY"].encode()
MCP_CAPABILITY = os.environ.get("MCP_CAPABILITY", "")
PUBLIC_CALLBACKS = [
    x.strip()
    for x in os.getenv(
        "PUBLIC_CALLBACKS",
        "https://mytrues-reader.ambitioushill-c7dc3aef.brazilsouth.azurecontainerapps.io/auth/callback,"
        "https://reader.mytrues.io/auth/callback",
    ).split(",")
    if x.strip()
]

app = FastAPI(title="MyTrues Human Reader", docs_url=None, redoc_url=None)

KIND_MAP = {
    "truth": "kind:truth",
    "observation": "kind:observation",
    "decision": "kind:decision",
    "preference": "kind:preference",
    "correction": "kind:correction",
}
RELATION_MAP = {
    "none": None,
    "continues": "key:continues",
    "corrects": "key:corrects",
    "confirms": "key:confirms",
    "contradicts": "key:contradicts",
    "based-on": "key:based-on",
    "influenced-by": "key:influenced-by",
}

MCP_TOOLS = [
    {
        "name": "memory_search",
        "description": "Search MyTrues historical memory by partial term and return related occurrences in chronological order.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "term": {"type": "string", "description": "Partial term to search, such as npm, pnpm, schema, OAuth, or a subject."}
            },
            "required": ["term"],
            "additionalProperties": False,
        },
        "annotations": {"readOnlyHint": True},
    },
    {
        "name": "memory_get",
        "description": "Fetch one MyTrues occurrence by its occurrence id.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "occurrence_id": {"type": "string", "description": "Occurrence id beginning with occ:"}
            },
            "required": ["occurrence_id"],
            "additionalProperties": False,
        },
        "annotations": {"readOnlyHint": True},
    },
    {
        "name": "memory_append",
        "description": "Append a new immutable occurrence to MyTrues memory. This never edits an older occurrence.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "subject": {"type": "string"},
                "statement": {"type": "string"},
                "kind": {
                    "type": "string",
                    "enum": ["truth", "observation", "decision", "preference", "correction"],
                    "default": "truth",
                },
                "relation": {
                    "type": "string",
                    "enum": ["none", "continues", "corrects", "confirms", "contradicts", "based-on", "influenced-by"],
                    "default": "none",
                },
                "related_occurrence": {"type": ["string", "null"]},
            },
            "required": ["subject", "statement"],
            "additionalProperties": False,
        },
        "annotations": {"readOnlyHint": False, "destructiveHint": False},
    },
    {
        "name": "memory_continue",
        "description": "Continue an existing cognitive history by appending a new occurrence linked to an earlier occurrence.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "related_occurrence": {"type": "string", "description": "Existing occurrence id to continue."},
                "subject": {"type": "string"},
                "statement": {"type": "string"},
                "kind": {
                    "type": "string",
                    "enum": ["truth", "observation", "decision", "preference", "correction"],
                    "default": "truth",
                },
                "relation": {
                    "type": "string",
                    "enum": ["continues", "corrects", "confirms", "contradicts", "based-on", "influenced-by"],
                    "default": "continues",
                },
            },
            "required": ["related_occurrence", "subject", "statement"],
            "additionalProperties": False,
        },
        "annotations": {"readOnlyHint": False, "destructiveHint": False},
    },
]


class OccurrenceCreate(BaseModel):
    subject: str = Field(min_length=1, max_length=240)
    statement: str = Field(min_length=3, max_length=4000)
    kind: str = Field(default="truth")
    relation: str = Field(default="none")
    related_occurrence: str | None = Field(default=None, max_length=200)


def b64(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).decode().rstrip("=")


def unb64(value: str) -> bytes:
    return base64.urlsafe_b64decode(value + "=" * (-len(value) % 4))


def sign_payload(payload: dict[str, Any]) -> str:
    raw = json.dumps(payload, separators=(",", ":"), ensure_ascii=False).encode()
    body = b64(raw)
    sig = b64(hmac.new(SESSION_KEY, body.encode(), hashlib.sha256).digest())
    return body + "." + sig


def read_payload(token: str | None) -> dict[str, Any] | None:
    if not token or "." not in token:
        return None
    body, sig = token.rsplit(".", 1)
    expected = b64(hmac.new(SESSION_KEY, body.encode(), hashlib.sha256).digest())
    if not hmac.compare_digest(sig, expected):
        return None
    try:
        payload = json.loads(unb64(body))
    except Exception:
        return None
    if payload.get("exp", 0) < time.time():
        return None
    return payload


def callback_for(request: Request) -> str:
    host = request.headers.get("x-forwarded-host") or request.headers.get("host", "")
    candidate = f"https://{host}/auth/callback"
    if candidate in PUBLIC_CALLBACKS:
        return candidate
    return PUBLIC_CALLBACKS[0]


def jwt_claims(token: str) -> dict[str, Any]:
    try:
        parts = token.split(".")
        if len(parts) != 3:
            return {}
        return json.loads(unb64(parts[1]))
    except Exception:
        return {}


def current_user(request: Request) -> dict[str, Any] | None:
    return read_payload(request.cookies.get("mt_session"))


def require_user(request: Request) -> dict[str, Any]:
    user = current_user(request)
    if not user:
        raise HTTPException(status_code=401, detail="authentication required")
    return user


def slug(text: str, limit: int = 80) -> str:
    value = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value).strip("-")
    return (value or "item")[:limit]


def q(value: str) -> str:
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n") + '"'


async def oauth_metadata(client: httpx.AsyncClient) -> dict[str, Any]:
    r = await client.get(f"{OAUTH_BASE}/.well-known/oauth-authorization-server", timeout=20)
    r.raise_for_status()
    return r.json()


async def typedb_access_token(client: httpx.AsyncClient) -> str:
    r = await client.post(
        f"{TYPEDB_URL}/v1/signin",
        json={"username": TYPEDB_USERNAME, "password": TYPEDB_PASSWORD},
        timeout=20,
    )
    r.raise_for_status()
    return r.json()["token"]


async def typedb_query(
    client: httpx.AsyncClient,
    access_token: str,
    query: str,
    transaction_type: str = "read",
    commit: bool = False,
    limit: int = 5000,
) -> dict[str, Any]:
    r = await client.post(
        f"{TYPEDB_URL}/v1/query",
        headers={"Authorization": f"Bearer {access_token}"},
        json={
            "databaseName": TYPEDB_DB,
            "transactionType": transaction_type,
            "commit": commit,
            "query": query,
            "queryOptions": {"includeInstanceTypes": False, "answerCountLimit": limit},
        },
        timeout=30,
    )
    if r.status_code >= 400:
        raise RuntimeError(f"TypeDB query failed: {r.status_code} {r.text[:800]}")
    return r.json()


def rows(response: dict[str, Any]) -> list[dict[str, Any]]:
    out = []
    for answer in response.get("answers") or []:
        data = answer.get("data") or {}
        out.append({k: v.get("value") for k, v in data.items() if isinstance(v, dict)})
    return out


async def atom_exists(client: httpx.AsyncClient, token: str, atom_id: str) -> bool:
    response = await typedb_query(
        client,
        token,
        f"match $a isa atom, has atom-id {q(atom_id)}; select $a;",
        limit=1,
    )
    return bool(response.get("answers"))


async def occurrence_exists(client: httpx.AsyncClient, token: str, occurrence_id: str) -> bool:
    response = await typedb_query(
        client,
        token,
        f"match $o isa occurrence, has atom-id {q(occurrence_id)}; select $o;",
        limit=1,
    )
    return bool(response.get("answers"))


async def transaction_open(client: httpx.AsyncClient, token: str) -> str:
    r = await client.post(
        f"{TYPEDB_URL}/v1/transactions/open",
        headers={"Authorization": f"Bearer {token}"},
        json={"databaseName": TYPEDB_DB, "transactionType": "write"},
        timeout=20,
    )
    r.raise_for_status()
    return r.json()["transactionId"]


async def transaction_query(client: httpx.AsyncClient, token: str, tx: str, query: str) -> None:
    r = await client.post(
        f"{TYPEDB_URL}/v1/transactions/{tx}/query",
        headers={"Authorization": f"Bearer {token}"},
        json={"query": query},
        timeout=30,
    )
    if r.status_code >= 400:
        raise RuntimeError(f"TypeDB transaction query failed: {r.status_code} {r.text[:800]}")


async def transaction_finish(client: httpx.AsyncClient, token: str, tx: str, action: str) -> None:
    r = await client.post(
        f"{TYPEDB_URL}/v1/transactions/{tx}/{action}",
        headers={"Authorization": f"Bearer {token}"},
        timeout=20,
    )
    r.raise_for_status()


async def read_memory(query_text: str = "") -> list[dict[str, Any]]:
    async with httpx.AsyncClient(follow_redirects=True) as client:
        token = await typedb_access_token(client)
        binding_response = await typedb_query(
            client,
            token,
            "match $o isa occurrence, has atom-id $oid; "
            "$b isa binding, links (occurrence: $o, key: $k, value: $v); "
            "$k has atom-id $key; $v has atom-id $value; "
            "select $oid, $key, $value;",
            limit=10000,
        )
        lexical_response = await typedb_query(
            client,
            token,
            "match $a isa atom, has atom-id $id, has lexical $lex; select $id, $lex;",
            limit=10000,
        )

    lexical = {r.get("id"): r.get("lex") for r in rows(lexical_response) if r.get("id")}
    grouped: dict[str, dict[str, Any]] = {}
    for row in rows(binding_response):
        oid, key, value = row.get("oid"), row.get("key"), row.get("value")
        if not oid or not key or not value:
            continue
        event = grouped.setdefault(oid, {"id": oid, "links": []})
        event["links"].append(
            {
                "key": key,
                "keyLexical": lexical.get(key, key.split(":", 1)[-1]),
                "value": value,
                "valueLexical": lexical.get(value, value.split(":", 1)[-1]),
            }
        )

    for event in grouped.values():
        time_link = next((x for x in event["links"] if x["key"] == "key:time"), None)
        event["time"] = (time_link or {}).get("valueLexical") or ""
        type_link = next((x for x in event["links"] if x["key"] == "key:type"), None)
        event["type"] = (type_link or {}).get("value") or ""

    events = list(grouped.values())
    needle = query_text.strip().casefold()
    if needle:
        direct = set()
        for event in events:
            hay = " ".join(
                [event["id"], event.get("type", "")]
                + [
                    str(v)
                    for link in event["links"]
                    for v in (
                        link["key"],
                        link["keyLexical"],
                        link["value"],
                        link["valueLexical"],
                    )
                ]
            ).casefold()
            if needle in hay:
                direct.add(event["id"])
        related = set(direct)
        for _ in range(2):
            for event in events:
                if event["id"] in related:
                    continue
                if any(link["value"] in related for link in event["links"]):
                    related.add(event["id"])
        events = [event for event in events if event["id"] in related]

    def sort_key(event: dict[str, Any]):
        raw = event.get("time") or ""
        try:
            return datetime.fromisoformat(raw.replace("Z", "+00:00"))
        except Exception:
            return datetime.min.replace(tzinfo=timezone.utc)

    events.sort(key=sort_key)
    return events


async def get_memory_occurrence(occurrence_id: str) -> dict[str, Any] | None:
    events = await read_memory("")
    return next((event for event in events if event["id"] == occurrence_id), None)


async def append_memory_occurrence(
    *,
    subject: str,
    statement: str,
    kind: str = "truth",
    relation: str = "none",
    related_occurrence: str | None = None,
    author_id: str = "auth:mcp-capability",
    author_lexical: str = "MCP capability client",
    provenance_id: str = "source:mcp",
    provenance_lexical: str = "MyTrues Memory MCP",
) -> dict[str, Any]:
    subject = subject.strip()
    statement = statement.strip()
    if not subject:
        raise HTTPException(status_code=400, detail="subject is required")
    if len(statement) < 3:
        raise HTTPException(status_code=400, detail="statement is too short")
    if kind not in KIND_MAP:
        raise HTTPException(status_code=400, detail="unsupported kind")
    if relation not in RELATION_MAP:
        raise HTTPException(status_code=400, detail="unsupported relation")

    relation_key = RELATION_MAP[relation]
    if relation_key and not related_occurrence:
        raise HTTPException(status_code=400, detail="related occurrence is required")
    if related_occurrence and not related_occurrence.startswith("occ:"):
        raise HTTPException(status_code=400, detail="invalid related occurrence")

    now = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    occ_id = f"occ:{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S')}-{uuid.uuid4().hex[:8]}"
    statement_id = "statement:" + hashlib.sha256(statement.encode()).hexdigest()[:20]
    subject_id = "subject:" + slug(subject)
    time_id = "time:" + now

    atoms: dict[str, str] = {
        "key:type": "type",
        "key:subject": "subject",
        "key:statement": "statement",
        "key:author": "author",
        "key:time": "time",
        "key:provenance": "provenance",
        KIND_MAP[kind]: kind,
        subject_id: subject,
        statement_id: statement,
        author_id: author_lexical,
        time_id: now,
        provenance_id: provenance_lexical,
    }
    if relation_key:
        atoms[relation_key] = relation_key.split(":", 1)[-1]

    bindings = [
        ("key:type", KIND_MAP[kind]),
        ("key:subject", subject_id),
        ("key:statement", statement_id),
        ("key:author", author_id),
        ("key:time", time_id),
        ("key:provenance", provenance_id),
    ]
    if relation_key and related_occurrence:
        bindings.append((relation_key, related_occurrence))

    async with httpx.AsyncClient(follow_redirects=True) as client:
        token = await typedb_access_token(client)
        if related_occurrence and not await occurrence_exists(client, token, related_occurrence):
            raise HTTPException(status_code=404, detail="related occurrence not found")

        tx = await transaction_open(client, token)
        try:
            for atom_id, lexical in atoms.items():
                exists = await atom_exists(client, token, atom_id)
                if not exists:
                    await transaction_query(
                        client,
                        token,
                        tx,
                        f"insert $a isa atom, has atom-id {q(atom_id)}, has lexical {q(lexical)};",
                    )

            await transaction_query(
                client,
                token,
                tx,
                f"insert $o isa occurrence, has atom-id {q(occ_id)}, has lexical {q(statement[:240])};",
            )

            for key_id, value_id in bindings:
                await transaction_query(
                    client,
                    token,
                    tx,
                    "match "
                    f"$o isa occurrence, has atom-id {q(occ_id)}; "
                    f"$k isa atom, has atom-id {q(key_id)}; "
                    f"$v isa atom, has atom-id {q(value_id)}; "
                    "insert $b isa binding, links (occurrence: $o, key: $k, value: $v);",
                )

            await transaction_finish(client, token, tx, "commit")
        except Exception:
            try:
                await transaction_finish(client, token, tx, "close")
            except Exception:
                pass
            raise

    created = await get_memory_occurrence(occ_id)
    return created or {"id": occ_id}


def mcp_text_result(payload: Any) -> dict[str, Any]:
    return {
        "content": [
            {
                "type": "text",
                "text": json.dumps(payload, ensure_ascii=False, indent=2),
            }
        ],
        "structuredContent": payload if isinstance(payload, dict) else {"result": payload},
        "isError": False,
    }


async def run_mcp_tool(name: str, arguments: dict[str, Any]) -> dict[str, Any]:
    if name == "memory_search":
        term = str(arguments.get("term") or "").strip()
        return mcp_text_result({"term": term, "events": await read_memory(term)})

    if name == "memory_get":
        occurrence_id = str(arguments.get("occurrence_id") or "").strip()
        event = await get_memory_occurrence(occurrence_id)
        if not event:
            return {
                "content": [{"type": "text", "text": f"Occurrence not found: {occurrence_id}"}],
                "isError": True,
            }
        return mcp_text_result(event)

    if name in {"memory_append", "memory_continue"}:
        relation = str(arguments.get("relation") or ("continues" if name == "memory_continue" else "none"))
        created = await append_memory_occurrence(
            subject=str(arguments.get("subject") or ""),
            statement=str(arguments.get("statement") or ""),
            kind=str(arguments.get("kind") or "truth"),
            relation=relation,
            related_occurrence=arguments.get("related_occurrence"),
        )
        return mcp_text_result({"created": created})

    return {
        "content": [{"type": "text", "text": f"Unknown tool: {name}"}],
        "isError": True,
    }


@app.post("/mcp/{capability}")
async def memory_mcp(capability: str, request: Request):
    if not MCP_CAPABILITY or not hmac.compare_digest(capability, MCP_CAPABILITY):
        raise HTTPException(status_code=404, detail="not found")

    try:
        payload = await request.json()
    except Exception:
        raise HTTPException(status_code=400, detail="invalid JSON")

    method = payload.get("method")
    request_id = payload.get("id")

    if method == "notifications/initialized":
        return JSONResponse({}, status_code=202)

    if method == "initialize":
        requested = (payload.get("params") or {}).get("protocolVersion") or "2025-06-18"
        return JSONResponse(
            {
                "jsonrpc": "2.0",
                "id": request_id,
                "result": {
                    "protocolVersion": requested,
                    "capabilities": {"tools": {"listChanged": False}},
                    "serverInfo": {"name": "MyTrues Memory MCP", "version": "0.1.0"},
                    "instructions": (
                        "Use memory_search and memory_get to inspect MyTrues historical memory. "
                        "Use memory_append or memory_continue to add immutable occurrences. "
                        "Never rewrite an old occurrence to represent a changed belief."
                    ),
                },
            }
        )

    if method == "ping":
        return JSONResponse({"jsonrpc": "2.0", "id": request_id, "result": {}})

    if method == "tools/list":
        return JSONResponse(
            {"jsonrpc": "2.0", "id": request_id, "result": {"tools": MCP_TOOLS}}
        )

    if method == "tools/call":
        params = payload.get("params") or {}
        try:
            result = await run_mcp_tool(str(params.get("name") or ""), params.get("arguments") or {})
            return JSONResponse({"jsonrpc": "2.0", "id": request_id, "result": result})
        except HTTPException as exc:
            return JSONResponse(
                {
                    "jsonrpc": "2.0",
                    "id": request_id,
                    "result": {
                        "content": [{"type": "text", "text": str(exc.detail)}],
                        "isError": True,
                    },
                }
            )
        except Exception as exc:
            return JSONResponse(
                {
                    "jsonrpc": "2.0",
                    "id": request_id,
                    "result": {
                        "content": [{"type": "text", "text": f"Memory tool failed: {exc}"}],
                        "isError": True,
                    },
                }
            )

    return JSONResponse(
        {
            "jsonrpc": "2.0",
            "id": request_id,
            "error": {"code": -32601, "message": f"Method not found: {method}"},
        }
    )


@app.get("/healthz")
async def healthz():
    return {"ok": True, "auth": OAUTH_BASE, "database": TYPEDB_DB}


@app.get("/login")
async def login(request: Request):
    redirect_uri = callback_for(request)
    verifier = secrets.token_urlsafe(48)
    challenge = b64(hashlib.sha256(verifier.encode()).digest())
    state = secrets.token_urlsafe(24)

    async with httpx.AsyncClient(follow_redirects=True) as client:
        metadata = await oauth_metadata(client)
        registration = await client.post(
            metadata["registration_endpoint"],
            json={
                "client_name": "MyTrues Human Reader",
                "redirect_uris": [redirect_uri],
                "grant_types": ["authorization_code", "refresh_token"],
                "response_types": ["code"],
                "token_endpoint_auth_method": "none",
            },
            timeout=20,
        )
        registration.raise_for_status()
        client_id = registration.json()["client_id"]

    tx = sign_payload(
        {
            "state": state,
            "verifier": verifier,
            "client_id": client_id,
            "redirect_uri": redirect_uri,
            "exp": time.time() + 600,
        }
    )
    params = {
        "response_type": "code",
        "client_id": client_id,
        "redirect_uri": redirect_uri,
        "scope": "openid",
        "code_challenge": challenge,
        "code_challenge_method": "S256",
        "state": state,
        "resource": f"{OAUTH_BASE}/mcp",
    }
    response = RedirectResponse(f"{OAUTH_BASE}/authorize?{urlencode(params)}", status_code=302)
    response.set_cookie(
        "mt_oauth_tx",
        tx,
        max_age=600,
        httponly=True,
        secure=True,
        samesite="lax",
    )
    return response


@app.get("/auth/callback")
async def auth_callback(request: Request, code: str | None = None, state: str | None = None):
    tx = read_payload(request.cookies.get("mt_oauth_tx"))
    if not tx or not code or not state or state != tx.get("state"):
        raise HTTPException(status_code=400, detail="invalid oauth transaction")

    async with httpx.AsyncClient(follow_redirects=True) as client:
        metadata = await oauth_metadata(client)
        token_response = await client.post(
            metadata["token_endpoint"],
            data={
                "grant_type": "authorization_code",
                "code": code,
                "client_id": tx["client_id"],
                "redirect_uri": tx["redirect_uri"],
                "code_verifier": tx["verifier"],
                "resource": f"{OAUTH_BASE}/mcp",
            },
            timeout=20,
        )
        token_response.raise_for_status()
        token_data = token_response.json()

    access_token = token_data.get("access_token") or ""
    id_token = token_data.get("id_token") or ""
    claims = jwt_claims(id_token) or jwt_claims(access_token)
    subject = str(claims.get("sub") or ("user:" + hashlib.sha256(access_token.encode()).hexdigest()[:20]))
    display = str(
        claims.get("name")
        or claims.get("preferred_username")
        or claims.get("email")
        or subject
    )

    session = sign_payload(
        {
            "sub": subject,
            "name": display,
            "iat": int(time.time()),
            "exp": time.time() + 8 * 3600,
        }
    )
    response = RedirectResponse("/", status_code=302)
    response.set_cookie(
        "mt_session",
        session,
        max_age=8 * 3600,
        httponly=True,
        secure=True,
        samesite="lax",
    )
    response.delete_cookie("mt_oauth_tx")
    return response


@app.get("/logout")
async def logout():
    response = RedirectResponse("/login", status_code=302)
    response.delete_cookie("mt_session")
    return response


@app.get("/api/me")
async def api_me(request: Request):
    user = require_user(request)
    return {"authenticated": True, "sub": user["sub"], "name": user.get("name") or user["sub"]}


@app.get("/api/history")
async def api_history(request: Request, q: str = ""):
    require_user(request)
    try:
        return {"events": await read_memory(q), "query": q}
    except Exception as exc:
        raise HTTPException(status_code=502, detail=f"memory query failed: {exc}") from exc


@app.post("/api/occurrences")
async def api_create_occurrence(request: Request, body: OccurrenceCreate):
    user = require_user(request)
    created = await append_memory_occurrence(
        subject=body.subject,
        statement=body.statement,
        kind=body.kind,
        relation=body.relation,
        related_occurrence=body.related_occurrence,
        author_id="auth:" + slug(str(user["sub"]), 120),
        author_lexical=str(user.get("name") or user["sub"]),
        provenance_id="source:reader",
        provenance_lexical="MyTrues Human Reader",
    )
    return JSONResponse({"created": created, "id": created["id"]}, status_code=201)


@app.get("/")
async def root(request: Request):
    if not current_user(request):
        return RedirectResponse("/login", status_code=302)
    return FileResponse(INDEX)


@app.get("/{path:path}")
async def spa_fallback(request: Request, path: str):
    if path.startswith("api/") or path.startswith("auth/"):
        raise HTTPException(status_code=404)
    if not current_user(request):
        return RedirectResponse("/login", status_code=302)
    return FileResponse(INDEX)
