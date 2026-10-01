#!/usr/bin/env python3
import argparse
import json
import os
import subprocess
import sys
import time


PROTOCOL_VERSION = "2026-07-28"


class MCPClient:
    def __init__(self, porter, allow_write=False):
        args = [porter, "mcp"]
        if allow_write:
            args.append("--allow-write")
        self.proc = subprocess.Popen(
            args,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            text=True,
            bufsize=1,
            env=os.environ.copy(),
        )
        self.next_id = 1
        self._request(
            "initialize",
            {
                "protocolVersion": PROTOCOL_VERSION,
                "capabilities": {},
                "clientInfo": {"name": "flowed-r1-probe", "version": "0.1"},
            },
        )
        self._notify("notifications/initialized", {})

    def _write(self, payload):
        self.proc.stdin.write(json.dumps(payload, separators=(",", ":")) + "\n")
        self.proc.stdin.flush()

    def _notify(self, method, params):
        self._write({"jsonrpc": "2.0", "method": method, "params": params})

    def _request(self, method, params):
        req_id = self.next_id
        self.next_id += 1
        self._write(
            {
                "jsonrpc": "2.0",
                "id": req_id,
                "method": method,
                "params": params,
            }
        )

        deadline = time.time() + 60
        while time.time() < deadline:
            line = self.proc.stdout.readline()
            if not line:
                if self.proc.poll() is not None:
                    raise RuntimeError(f"MCP server exited with {self.proc.returncode}")
                continue
            msg = json.loads(line)
            if msg.get("id") == req_id:
                if "error" in msg:
                    raise RuntimeError(json.dumps(msg["error"]))
                return msg["result"]
        raise TimeoutError(method)

    def tools(self):
        return self._request("tools/list", {}).get("tools", [])

    def call(self, name, arguments):
        return self._request(
            "tools/call",
            {"name": name, "arguments": arguments},
        )

    def close(self):
        if self.proc.poll() is None:
            self.proc.terminate()
            try:
                self.proc.wait(timeout=10)
            except subprocess.TimeoutExpired:
                self.proc.kill()


def text_from_tool(result):
    return "\n".join(
        item.get("text", "")
        for item in result.get("content", [])
        if item.get("type") == "text"
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--porter", required=True)
    parser.add_argument("--reference", required=True)
    args = parser.parse_args()

    read = MCPClient(args.porter, allow_write=False)
    try:
        read_tools = {tool["name"] for tool in read.tools()}
        required_read = {
            "list_installations",
            "show_installation",
            "list_outputs",
            "get_output",
            "list_credentials",
            "list_parameters",
            "analyze_failure",
        }
        missing = required_read - read_tools
        assert not missing, f"missing read tools: {sorted(missing)}"
        assert "install_bundle" not in read_tools
        assert "uninstall_bundle" not in read_tools

        installs = text_from_tool(
            read.call(
                "list_installations",
                {"namespace": "r1-default", "name": "native-cli"},
            )
        )
        assert "native-cli" in installs

        outputs = text_from_tool(
            read.call(
                "list_outputs",
                {"installation": "native-cli", "namespace": "r1-default"},
            )
        )
        assert "sensitive-marker" in outputs
        assert "***" in outputs
        assert "sensitive-output" not in outputs

        sensitive = read.call(
            "get_output",
            {
                "installation": "native-cli",
                "namespace": "r1-default",
                "output_name": "sensitive-marker",
            },
        )
        assert sensitive.get("isError") is True
        assert "sensitive" in text_from_tool(sensitive).lower()

        print("MCP_READ_ONLY_SURFACE=PASS")
        print("MCP_SENSITIVE_OUTPUT_PROTECTION=PASS")
    finally:
        read.close()

    write = MCPClient(args.porter, allow_write=True)
    try:
        write_tools = {tool["name"] for tool in write.tools()}
        required_write = {
            "install_bundle",
            "upgrade_bundle",
            "uninstall_bundle",
            "invoke_bundle",
        }
        missing = required_write - write_tools
        assert not missing, f"missing write tools: {sorted(missing)}"

        installed = write.call(
            "install_bundle",
            {
                "name": "native-mcp",
                "namespace": "r1-default",
                "reference": args.reference,
                "credential_sets": ["r1creds"],
                "parameter_sets": ["r1params"],
            },
        )
        assert installed.get("isError") is not True, text_from_tool(installed)

        invoked = write.call(
            "invoke_bundle",
            {
                "name": "native-mcp",
                "namespace": "r1-default",
                "action": "status",
                "params": {"greeting": "from-mcp"},
            },
        )
        assert invoked.get("isError") is not True, text_from_tool(invoked)

        mcp_outputs = text_from_tool(
            write.call(
                "list_outputs",
                {"installation": "native-mcp", "namespace": "r1-default"},
            )
        )
        assert "install:from-parameter-set" in mcp_outputs

        uninstalled = write.call(
            "uninstall_bundle",
            {"name": "native-mcp", "namespace": "r1-default"},
        )
        assert uninstalled.get("isError") is not True, text_from_tool(uninstalled)

        print("MCP_WRITE_SURFACE=PASS")
        print("MCP_INSTALL_INVOKE_UNINSTALL=PASS")
    finally:
        write.close()


if __name__ == "__main__":
    main()
