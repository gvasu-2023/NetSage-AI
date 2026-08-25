def diagnose_dhcp_service_failure(case_data):
    """
    Detect whether a DHCP service is disabled or unavailable.
    """

    if case_data.get("category") != "DHCP":
        return {
            "fault_detected": False
        }

    dhcp_data = case_data.get("dhcp", {})
    symptoms = case_data.get("symptoms", {})

    service_enabled = dhcp_data.get("service_enabled")
    client_ip = symptoms.get("dhcp_client_ip_address")
    default_gateway = symptoms.get(
        "dhcp_client_default_gateway"
    )

    is_apipa_address = (
        isinstance(client_ip, str)
        and client_ip.startswith("169.254.")
    )

    has_no_gateway = default_gateway == "0.0.0.0"

    if (
        service_enabled is False
        and is_apipa_address
        and has_no_gateway
    ):
        return {
            "fault_detected": True,
            "category": "DHCP",
            "diagnosis": "DHCP Service Failure",
            "faulty_device": dhcp_data.get("server"),
            "osi_layer": case_data.get("osi_layer"),
            "confidence": "High",
            "dhcp_service_enabled": service_enabled,
            "dhcp_client_ip_address": client_ip,
            "expected_network": symptoms.get(
                "expected_network"
            ),
            "explanation": (
                f"The DHCP service on "
                f"{dhcp_data.get('server')} is disabled. "
                f"The DHCP client received the APIPA address "
                f"{client_ip} instead of a valid address from "
                f"{symptoms.get('expected_network')}."
            ),
            "recommended_fix": (
                f"Enable the DHCP service on "
                f"{dhcp_data.get('server')} and verify that the "
                f"DHCP pool configuration is active."
            )
        }

    return {
        "fault_detected": False
    }