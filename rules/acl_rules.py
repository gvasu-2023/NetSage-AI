def diagnose_acl_blocks_traffic(case_data):
    """
    Diagnose a connectivity failure caused by an ACL
    explicitly blocking traffic between a source and
    destination host.
    """

    if case_data.get("category") != "ACL":
        return {
            "fault_detected": False
        }

    topology = case_data.get("topology", {})
    acl_data = case_data.get("acl_configuration", {})
    expected_data = case_data.get("expected_diagnosis", {})

    deny_rule_present = acl_data.get(
        "deny_rule_present",
        False
    )

    acl_match = case_data.get(
        "symptoms",
        {}
    ).get(
        "acl_match",
        False
    )

    if not deny_rule_present and not acl_match:
        return {
            "fault_detected": False
        }

    faulty_device = topology.get(
        "faulty_device"
    )

    faulty_interface = topology.get(
        "outgoing_interface"
    )

    acl_number = acl_data.get(
        "acl_number"
    )

    acl_direction = acl_data.get(
        "acl_direction"
    )

    blocked_source = acl_data.get(
        "blocked_source"
    )

    blocked_destination = acl_data.get(
        "blocked_destination"
    )

    return {
        "fault_detected": True,
        "category": "ACL",
        "diagnosis": "ACL Blocking Traffic",
        "faulty_device": faulty_device,
        "faulty_interface": faulty_interface,
        "osi_layer": expected_data.get(
            "osi_layer",
            "Layer 3"
        ),
        "confidence": expected_data.get(
            "confidence",
            "High"
        ),
        "acl_number": acl_number,
        "acl_direction": acl_direction,
        "blocked_source": blocked_source,
        "blocked_destination": blocked_destination,
        "deny_rule_present": deny_rule_present,
        "explanation": (
            f"ACL {acl_number} on {faulty_device} is applied "
            f"in the {acl_direction} direction on interface "
            f"{faulty_interface} and contains a deny rule that "
            f"blocks traffic from {blocked_source} to "
            f"{blocked_destination}."
        ),
        "recommended_fix": (
            f"Remove or modify the deny rule in ACL {acl_number} "
            f"on {faulty_device} so that traffic from "
            f"{blocked_source} to {blocked_destination} is "
            f"permitted."
        )
    }