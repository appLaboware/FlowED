CASES = {
    "dns.requested_provider_credentials_missing": [
        {
            "id": "decision.dns.use_azure_provider_fqdn",
            "status": "approved",
            "risk": "low",
            "automation": "automatic",
            "action": "delivery.use_provider_endpoint",
            "endpoint_type": "hostname",
            "context_key": "azure_provider_fqdn",
            "guard": "azure_provider_fqdn_available",
            "notice": (
                "Custom DNS is unavailable; deployment continued using "
                "the Azure-provided hostname."
            ),
        },
        {
            "id": "decision.dns.expose_public_ip",
            "status": "approved",
            "risk": "low",
            "automation": "automatic",
            "action": "delivery.use_provider_endpoint",
            "endpoint_type": "ip",
            "context_key": "azure_public_ip",
            "guard": "azure_public_ip_available",
            "notice": (
                "Custom DNS is unavailable; deployment continued by "
                "exposing the public IP of the Azure workload."
            ),
        },
    ]
}
