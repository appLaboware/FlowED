# RESULTS — EXP-003 Azure trust/bootstrap

Status: **PARTIAL — authentication/authorization proved; EXP-003 materialization not executed.**

## Evidence A — GitHub Actions OIDC to Azure

Successful run:

- workflow: `IDEOS Azure OIDC direct proof`
- run: `36795844036`
- conclusion: `success`

The run executed and passed:

1. Azure identifier resolution;
2. GitHub OIDC token request;
3. federated service-principal login;
4. read access to the laboratory Resource Group;
5. a Contributor-scoped write operation using an empty ARM deployment;
6. cleanup of the proof deployment record.

Therefore the following claim is supported by **EVIDENCE-A**:

`GitHub Actions -> OIDC -> Azure -> RG read -> Contributor write`

No long-lived Azure client secret was required.

## Not proved inside EXP-003

The workflow `.github/workflows/ideos-azure-e2e.yml` exists and describes:

`create ACI -> obtain FQDN -> verify HTTP -> destroy ACI`

During this audit, no Actions run of `IDEOS Azure end-to-end materialization` was
found in the inspected branch run history.

Classification:

- workflow definition: **EVIDENCE-D**;
- ACI materialization claim *within EXP-003*: **NOT PROVEN**.

Azure materialization was proved later by other experiments, but that evidence is
not retroactively attributed to EXP-003.

## One-time bootstrap boundary

`bootstrap-rbac.sh` creates/converges Azure identity, federated credential and RBAC.

It is intentionally a privileged bootstrap operation. It was not exercised by the
current GitHub Actions identity because doing so would require widening the same
identity's authority to create identity/RBAC state.

Classification: **not executable in current Actions trust scope by design**.

## Honest conclusion

EXP-003 proved the non-secret operational authentication path and Resource Group
write scope. It did not, by itself, complete its proposed reversible application
materialization workflow.
