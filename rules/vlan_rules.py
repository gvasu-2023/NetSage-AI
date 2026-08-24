def diagnose_vlan_assignment(case_data):
    """
    Detect a wrong VLAN assignment on a switch access interface.

    Returns a diagnosis when the actual VLAN does not match
    the expected VLAN.
    """

    device_configs = case_data.get("device_configs", {})
    switch_config = device_configs.get("SW1", {})

    actual_vlan = switch_config.get("actual_vlan")
    expected_vlan = switch_config.get("expected_vlan")
    faulty_interface = switch_config.get("faulty_interface")

    if actual_vlan is None or expected_vlan is None:
        return {
            "fault_detected": False
        }

    if actual_vlan != expected_vlan:
        return {
            "fault_detected": True,
            "category": "VLAN",
            "diagnosis": "Wrong VLAN Assignment",
            "faulty_device": "SW1",
            "faulty_interface": faulty_interface,
            "actual_vlan": actual_vlan,
            "expected_vlan": expected_vlan,
            "osi_layer": "Layer 2",
            "confidence": "High",
            "explanation": (
                f"SW1 interface {faulty_interface} is assigned to VLAN "
                f"{actual_vlan}, but the expected VLAN is {expected_vlan}."
            ),
            "recommended_fix": (
                f"Change SW1 interface {faulty_interface} from VLAN "
                f"{actual_vlan} to VLAN {expected_vlan}."
            )
        }

    return {
        "fault_detected": False
    }