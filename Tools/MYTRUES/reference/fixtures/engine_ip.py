from engine_port import DecisionEngine


class Engine(DecisionEngine):
    """Conformance fixture only. Not the MyTrues proprietary algorithm."""

    name = "reference-ip-fixture"
    version = "0.1"

    def choose(self, request, candidates):
        context = request["context"]
        for candidate in candidates:
            if candidate["id"] == "decision.dns.expose_public_ip":
                if context.get("azure_public_ip_available") and context.get("azure_public_ip"):
                    return candidate
        raise LookupError("no approved IP candidate")
