def diagnose_interface_administratively_down(case_data):
    """
    Diagnose a switch interface that is administratively down.
    """

    if case_data.get("category") != "Interface":
        return {
            "fault_detected": False
        }

    interface_data = case_data.get("interface", {})
    expected_state = case_data.get("expected_state", {})
    topology = case_data.get("topology", {})

    admin_status = interface_data.get("admin_status")
    expected_admin_status = expected_state.get("admin_status")

    status_reason = (
        interface_data.get("status_reason", "")
        .lower()
        .strip()
    )

    if (
        admin_status == "down"
        and expected_admin_status == "up"
        and "administratively down" in status_reason
    ):
        return {
            "fault_detected": True,
            "category": "Interface",
            "diagnosis": "Interface Administratively Down",
            "faulty_device": topology.get("faulty_device"),
            "faulty_interface": topology.get("faulty_interface"),
            "osi_layer": "Layer 1/2",
            "confidence": "High",
            "admin_status": admin_status,
            "expected_admin_status": expected_admin_status,
            "oper_status": interface_data.get("oper_status"),
            "connected_device": topology.get("connected_device"),
            "explanation": (
                f"{topology.get('faulty_device')} interface "
                f"{topology.get('faulty_interface')} is administratively "
                f"down. The interface is expected to be enabled and "
                f"connected to {topology.get('connected_device')}."
            ),
            "recommended_fix": (
                f"Enable {topology.get('faulty_interface')} on "
                f"{topology.get('faulty_device')} using the "
                f"'no shutdown' command."
            )
        }

    return {
        "fault_detected": False
    }