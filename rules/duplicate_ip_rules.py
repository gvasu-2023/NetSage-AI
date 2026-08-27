def diagnose_duplicate_ip_address(case_data):
    """
    Diagnose a duplicate IPv4 address conflict.
    """

    if case_data.get("category") != "IP Configuration":
        return {
            "fault_detected": False
        }

    topology = case_data.get("topology", {})
    ip_data = case_data.get("ip_configuration", {})
    symptoms = case_data.get("symptoms", {})

    duplicate_ip_detected = ip_data.get(
        "duplicate_ip_detected",
        False
    )

    pc1_ip_address = ip_data.get("pc1_ip_address")
    pc3_ip_address = ip_data.get("pc3_ip_address")

    ip_conflict_detected = symptoms.get(
        "ip_conflict_detected",
        False
    )

    gateway_ping_failed = (
        symptoms.get("gateway_ping") == "failed"
    )

    remote_ping_failed = (
        symptoms.get("remote_ping") == "failed"
    )

    if (
        not duplicate_ip_detected
        or pc1_ip_address != pc3_ip_address
        or not ip_conflict_detected
        or not gateway_ping_failed
        or not remote_ping_failed
    ):
        return {
            "fault_detected": False
        }

    faulty_device = topology.get("faulty_device")
    conflicting_device = topology.get(
        "conflicting_device"
    )
    duplicate_ip_address = ip_data.get(
        "duplicate_ip_address"
    )
    expected_pc3_ip = ip_data.get(
        "expected_pc3_ip"
    )
    affected_network = topology.get(
        "affected_network"
    )
    default_gateway = topology.get(
        "default_gateway"
    )

    return {
        "fault_detected": True,
        "category": "IP Configuration",
        "diagnosis": "Duplicate IP Address",
        "faulty_device": faulty_device,
        "conflicting_device": conflicting_device,
        "duplicate_ip_address": duplicate_ip_address,
        "expected_ip_address": expected_pc3_ip,
        "affected_network": affected_network,
        "default_gateway": default_gateway,
        "osi_layer": "Layer 3",
        "confidence": "High",
        "explanation": (
            f"{faulty_device} and {conflicting_device} "
            f"are both configured with the IP address "
            f"{duplicate_ip_address} on network "
            f"{affected_network}. This creates an IP "
            f"address conflict and prevents reliable "
            f"communication."
        ),
        "recommended_fix": (
            f"Assign a unique IP address to "
            f"{faulty_device}. Configure "
            f"{faulty_device} with "
            f"{expected_pc3_ip} and ensure that "
            f"{conflicting_device} retains "
            f"{duplicate_ip_address}. Use subnet mask "
            f"255.255.255.0 and default gateway "
            f"{default_gateway}."
        )
    }