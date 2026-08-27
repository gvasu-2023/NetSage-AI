def diagnose_dhcp_relay_missing(case_data):
    """
    Diagnose a DHCP failure caused by a missing DHCP relay
    configuration on a router interface.
    """

    if case_data.get("category") != "DHCP Relay":
        return {
            "fault_detected": False
        }

    topology = case_data.get("topology", {})
    relay_data = case_data.get("dhcp_relay", {})
    symptoms = case_data.get("symptoms", {})

    helper_address_configured = relay_data.get(
        "helper_address_configured",
        False
    )

    dhcp_request_failed = (
        symptoms.get("dhcp_request") == "failed"
    )

    apipa_assigned = symptoms.get(
        "apipa_assigned",
        False
    )

    if (
        helper_address_configured
        or not dhcp_request_failed
        or not apipa_assigned
    ):
        return {
            "fault_detected": False
        }

    faulty_device = topology.get("faulty_device")
    faulty_interface = topology.get("faulty_interface")
    dhcp_server = topology.get("dhcp_server")
    expected_helper_address = relay_data.get(
        "expected_helper_address"
    )

    return {
        "fault_detected": True,
        "category": "DHCP Relay",
        "diagnosis": "DHCP Relay Missing",
        "faulty_device": faulty_device,
        "faulty_interface": faulty_interface,
        "osi_layer": "Layer 3",
        "confidence": "High",
        "client_device": topology.get("client_device"),
        "client_network": topology.get("client_network"),
        "dhcp_server": dhcp_server,
        "dhcp_server_ip": topology.get(
            "dhcp_server_ip"
        ),
        "helper_address_configured": helper_address_configured,
        "expected_helper_address": expected_helper_address,
        "client_ip_address": symptoms.get(
            "client_ip_address"
        ),
        "apipa_assigned": apipa_assigned,
        "explanation": (
            f"{faulty_device} interface {faulty_interface} "
            f"is missing the DHCP relay configuration required "
            f"to forward DHCP requests from "
            f"{topology.get('client_device')} on "
            f"{topology.get('client_network')} to "
            f"{dhcp_server} at {expected_helper_address}. "
            f"As a result, the DHCP request fails and the client "
            f"receives an APIPA address."
        ),
        "recommended_fix": (
            f"Configure 'ip helper-address "
            f"{expected_helper_address}' on "
            f"{faulty_device} interface {faulty_interface}."
        )
    }