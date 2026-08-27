def diagnose_native_vlan_mismatch(case_data):
    """
    Diagnose a native VLAN mismatch on a trunk connection.
    """

    if case_data.get("category") != "VLAN":
        return {
            "fault_detected": False
        }

    topology = case_data.get("topology", {})
    native_vlan_data = case_data.get(
        "native_vlan",
        {}
    )
    symptoms = case_data.get("symptoms", {})

    local_native_vlan = native_vlan_data.get(
        "local_native_vlan"
    )
    remote_native_vlan = native_vlan_data.get(
        "remote_native_vlan"
    )

    mismatch_detected = (
        native_vlan_data.get(
            "mismatch_detected",
            False
        )
        and local_native_vlan is not None
        and remote_native_vlan is not None
        and local_native_vlan != remote_native_vlan
    )

    affected_gateway_ping_failed = (
        symptoms.get(
            "affected_vlan_gateway_ping"
        ) == "failed"
    )

    affected_remote_ping_failed = (
        symptoms.get(
            "affected_vlan_remote_ping"
        ) == "failed"
    )

    if (
        not mismatch_detected
        or not affected_gateway_ping_failed
        or not affected_remote_ping_failed
    ):
        return {
            "fault_detected": False
        }

    faulty_device = topology.get("faulty_device")
    faulty_interface = topology.get(
        "faulty_interface"
    )
    connected_device = topology.get(
        "connected_device"
    )
    connected_interface = topology.get(
        "connected_interface"
    )
    affected_vlan = topology.get("affected_vlan")

    return {
        "fault_detected": True,
        "category": "VLAN",
        "diagnosis": "Native VLAN Mismatch",
        "faulty_device": faulty_device,
        "faulty_interface": faulty_interface,
        "connected_device": connected_device,
        "connected_interface": connected_interface,
        "affected_vlan": affected_vlan,
        "local_native_vlan": local_native_vlan,
        "remote_native_vlan": remote_native_vlan,
        "osi_layer": "Layer 2",
        "confidence": "High",
        "explanation": (
            f"The trunk connection between "
            f"{faulty_device} interface {faulty_interface} "
            f"and {connected_device} interface "
            f"{connected_interface} has a native VLAN mismatch. "
            f"{faulty_device} uses native VLAN "
            f"{local_native_vlan}, while "
            f"{connected_device} uses native VLAN "
            f"{remote_native_vlan}. "
            f"This causes untagged traffic to be interpreted "
            f"as belonging to different VLANs and affects "
            f"connectivity for VLAN {affected_vlan}."
        ),
        "recommended_fix": (
            f"Configure the same native VLAN on both sides "
            f"of the trunk. Verify that "
            f"{faulty_device} interface {faulty_interface} "
            f"and {connected_device} interface "
            f"{connected_interface} use the same native VLAN."
        )
    }