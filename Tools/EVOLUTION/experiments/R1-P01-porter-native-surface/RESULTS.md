# RESULTS — R1-P01

Status: **PASS**

GitHub Actions evidence:

- run: `36818953832`
- Porter: `v1.6.1 (c28b780c)`

## Native capabilities reproduced

- named configuration contexts;
- parameter sets;
- credential sets;
- install / upgrade / uninstall;
- bundle outputs;
- sensitive outputs stored through the lab filesystem secrets plugin;
- stateless custom action with `modifies: false`;
- OCI publish to a local registry;
- inspect of a published bundle;
- bundle archive;
- built-in Porter MCP server;
- MCP read-only surface by default;
- MCP write operations only with `--allow-write`;
- MCP install / invoke / uninstall;
- MCP masking/blocking of sensitive outputs.

## Parameter precedence proof

Install used:

`r1params -> greeting=from-parameter-set`

and produced:

`install:from-parameter-set`

Upgrade used a direct CLI override:

`--param greeting=from-cli-override`

and produced:

`upgrade:from-cli-override`

This confirms the expected higher precedence of direct parameter override over a stored
parameter-set value for this path.

## Credential proof

The credential set stored only the source mapping (`env: LAB_TOKEN`).
The resolved synthetic credential was required by the invocation but was not exposed by
`porter credentials show`.

## MCP proof

Read-only mode exposed inspection/state tools and did not register lifecycle mutations.

Write mode registered:

- `install_bundle`;
- `upgrade_bundle`;
- `uninstall_bundle`;
- `invoke_bundle`.

The experiment installed the published OCI bundle through MCP, invoked its custom action
and uninstalled it successfully.

### Sensitive outputs

The local Porter CLI can display sensitive output values to the local authorized operator.
The MCP surface behaves more restrictively:

- `list_outputs` masks the value as `***`;
- `get_output` refuses to return a sensitive output.

Do not conflate local CLI visibility with MCP policy.

## Confirmed MCP protocol defect / integration limit

During write operations, Porter v1.6.1 emitted non-JSON text on **stdout** while running
the stdio MCP server:

- `Just-in-time resolving credentials...`
- `Just-in-time resolving parameters...`
- `uninstalling bundle`

The Go MCP transport used by Porter defines stdio as newline-delimited JSON. Therefore
these lines pollute the protocol stream for strict MCP clients.

Our probe ignored the non-JSON lines only to determine whether Porter eventually returned
valid tool responses. It did, and lifecycle actions succeeded.

Classification:

- capability works;
- stdio purity is a **confirmed interoperability defect in this environment**;
- do not build a proprietary workaround into IDEOS yet;
- search/report upstream first.

## Consequence for IDEOS

The hypothesis that IDEOS needs to invent its own "AI/intent bridge to Porter" is weakened.

Porter 1.6.1 already includes a first-party MCP server with both inspection and explicitly
opt-in lifecycle mutation tools. We must exhaust and harden that path before adding a
parallel intent/agent API.

Evidence class: **EVIDENCE-B** (reproducible integration/conformance execution).
