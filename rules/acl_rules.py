def diagnose_acl_blocks_traffic(case_data):
    """
    Diagnose a connectivity failure caused by an ACL
    explicitly denying traffic between the source and
    destination hosts.
    """

    if case_data.get("category") != "ACL":
        return {
            "fault_detected": False
        }

    topology = case_data.get("topology", {})
    acl_data = case_data.get("acl", {})

    action = acl_data.get("action")

    if action == "deny":
        faulty_device = topology.get("faulty_device")
        faulty_interface = topology.get("faulty_interface")

        source_ip = acl_data.get(
            "source",
            topology.get("source_ip")
        )

        destination_ip = acl_data.get(
            "destination",
            topology.get("destination_ip")
        )

        acl_number = acl_data.get("acl_number")
        direction = acl_data.get("direction")

        return {
            "fault_detected": True,
            "category": "ACL",
            "diagnosis": "ACL Blocks Traffic",
            "faulty_device": faulty_device,
            "faulty_interface": faulty_interface,
            "osi_layer": "Layer 3",
            "confidence": "High",
            "acl_number": acl_number,
            "acl_direction": direction,
            "blocked_source": source_ip,
            "blocked_destination": destination_ip,
            "configured_action": action,
            "explanation": (
                f"ACL {acl_number} on {faulty_device} contains a deny rule "
                f"that blocks traffic from {source_ip} to {destination_ip}."
            ),
            "recommended_fix": (
                f"Remove or modify the deny rule in ACL {acl_number} on "
                f"{faulty_device} so that traffic from {source_ip} to "
                f"{destination_ip} is permitted."
            )
        }

    return {
        "fault_detected": False
    }