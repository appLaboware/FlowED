from engine_port import DecisionEngine


class Engine(DecisionEngine):
    """Conformance fixture only. Not the MyTrues proprietary algorithm."""

    name = "reference-fqdn-fixture"
    version = "0.1"

    def choose(self, request, candidates):
        context = request["context"]
        for candidate in candidates:
            if candidate["id"] == "decision.dns.use_azure_provider_fqdn":
                if context.get("azure_provider_fqdn_available") and context.get("azure_provider_fqdn"):
                    return candidate
        raise LookupError("no approved FQDN candidate")
