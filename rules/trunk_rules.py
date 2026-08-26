def diagnose_vlan_missing_from_trunk(case_data):
    """
    Diagnose whether a required VLAN is missing from a trunk.
    """

    trunk = case_data.get("trunk")

    if not trunk:
        return {
            "fault_detected": False
        }

    actual_allowed_vlans = trunk.get("actual_allowed_vlans", [])

    expected_state = case_data.get(
        "expected_state",
        {}
    )

    required_vlan = expected_state.get(
        "required_vlan"
    )

    if (
        required_vlan is None
        or required_vlan in actual_allowed_vlans
    ):
        return {
            "fault_detected": False
        }

    topology = case_data.get(
        "topology",
        {}
    )

    faulty_device = topology.get(
        "faulty_device"
    )

    faulty_interface = trunk.get(
        "interface"
    )

    return {
        "fault_detected": True,
        "category": "VLAN",
        "diagnosis": "VLAN Missing From Trunk",
        "faulty_device": faulty_device,
        "faulty_interface": faulty_interface,
        "osi_layer": "Layer 2",
        "confidence": "High",
        "missing_vlan": required_vlan,
        "actual_allowed_vlans": actual_allowed_vlans,
        "explanation": (
            f"{faulty_device} interface "
            f"{faulty_interface} does not allow "
            f"VLAN {required_vlan} on the trunk. "
            f"Traffic for VLAN {required_vlan} "
            "cannot traverse the trunk to the router."
        ),
        "recommended_fix": (
            f"Allow VLAN {required_vlan} on the "
            f"trunk interface {faulty_interface} "
            f"using: switchport trunk allowed vlan "
            f"add {required_vlan}"
        )
    }