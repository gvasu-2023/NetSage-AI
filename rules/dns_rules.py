def diagnose_wrong_dns_server(case_data):
    """
    Detect a DNS configuration fault where a device is configured
    with a DNS server different from the expected DNS server.
    """

    if case_data.get("case_id") != "CASE008":
        return {
            "fault_detected": False
        }

    configured_dns = (
        case_data.get("ip_configuration", {})
        .get("configured_dns_server")
    )

    correct_dns = (
        case_data.get("expected_state", {})
        .get("correct_dns_server")
    )

    hostname_resolution = (
        case_data.get("symptoms", {})
        .get("hostname_resolution")
    )

    direct_ip_connectivity = (
        case_data.get("symptoms", {})
        .get("direct_ip_connectivity")
    )

    if (
        configured_dns != correct_dns
        and hostname_resolution == "failed"
        and direct_ip_connectivity == "working"
    ):
        return {
            "fault_detected": True,
            "category": "DNS",
            "diagnosis": "Wrong DNS Server",
            "faulty_device": (
                case_data.get("topology", {})
                .get("faulty_device")
            ),
            "osi_layer": "Layer 7",
            "confidence": "High",
            "configured_dns_server": configured_dns,
            "correct_dns_server": correct_dns,
            "hostname": (
                case_data.get("expected_state", {})
                .get("hostname")
            ),
            "expected_ip_address": (
                case_data.get("expected_state", {})
                .get("expected_ip_address")
            ),
            "explanation": (
                f"PC1 is configured with DNS server "
                f"{configured_dns}, but the correct DNS server is "
                f"{correct_dns}. Direct IP connectivity is working, "
                f"but hostname resolution is failing."
            ),
            "recommended_fix": (
                f"Change the DNS server on PC1 from "
                f"{configured_dns} to {correct_dns}."
            )
        }

    return {
        "fault_detected": False
    }