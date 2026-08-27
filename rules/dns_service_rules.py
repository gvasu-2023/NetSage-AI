def diagnose_dns_service_failure(case_data):
    """
    Diagnose a DNS service failure.
    """

    if case_data.get("category") != "DNS":
        return {
            "fault_detected": False
        }

    topology = case_data.get("topology", {})
    dns_service = case_data.get("dns_service", {})
    symptoms = case_data.get("symptoms", {})

    service_status = dns_service.get(
        "service_status"
    )

    configured_dns_server = dns_service.get(
        "configured_dns_server"
    )

    dns_server_ip = topology.get(
        "dns_server_ip"
    )

    dns_record_exists = dns_service.get(
        "dns_record_exists",
        False
    )

    direct_ip_connectivity_working = (
        symptoms.get(
            "direct_ip_connectivity"
        ) == "working"
    )

    hostname_resolution_failed = (
        symptoms.get(
            "hostname_resolution"
        ) == "failed"
    )

    if (
        service_status != "OFF"
        or configured_dns_server != dns_server_ip
        or not dns_record_exists
        or not direct_ip_connectivity_working
        or not hostname_resolution_failed
    ):
        return {
            "fault_detected": False
        }

    faulty_device = topology.get(
        "faulty_device"
    )

    dns_client = topology.get(
        "dns_client"
    )

    hostname = topology.get(
        "hostname"
    )

    expected_ip_address = topology.get(
        "expected_ip_address"
    )

    return {
        "fault_detected": True,
        "category": "DNS",
        "diagnosis": "DNS Service Failure",
        "faulty_device": faulty_device,
        "osi_layer": "Layer 7",
        "confidence": "High",
        "configured_dns_server": configured_dns_server,
        "hostname": hostname,
        "expected_ip_address": expected_ip_address,
        "dns_service_status": service_status,
        "explanation": (
            f"{dns_client} is configured with the correct DNS "
            f"server {configured_dns_server}, and direct IP "
            f"connectivity is working. However, the DNS service "
            f"on {faulty_device} is disabled, so hostname "
            f"{hostname} cannot be resolved to "
            f"{expected_ip_address}."
        ),
        "recommended_fix": (
            f"Enable the DNS service on {faulty_device} and "
            f"verify that the DNS record for {hostname} "
            f"resolves to {expected_ip_address}."
        )
    }