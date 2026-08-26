def diagnose_port_security_violation(case_data):
    """
    Diagnose a switch interface disabled because of
    a port security violation.
    """

    if case_data.get("category") != "Port Security":
        return {
            "fault_detected": False
        }

    topology = case_data.get("topology", {})
    security_data = case_data.get("port_security", {})
    expected_data = case_data.get("expected", {})

    port_status = security_data.get("port_status")
    violation_count = security_data.get(
        "security_violation_count",
        0
    )
    interface_status = security_data.get(
        "interface_status"
    )

    violation_detected = (
        port_status == "Secure-shutdown"
        or violation_count > 0
        or interface_status == "err-disabled"
    )

    if not violation_detected:
        return {
            "fault_detected": False
        }

    faulty_device = topology.get("faulty_device")
    faulty_interface = topology.get("faulty_interface")

    return {
        "fault_detected": True,
        "category": "Port Security",
        "diagnosis": "Port Security Violation",
        "faulty_device": faulty_device,
        "faulty_interface": faulty_interface,
        "osi_layer": "Layer 2",
        "confidence": "High",
        "port_status": port_status,
        "violation_mode": security_data.get(
            "violation_mode"
        ),
        "maximum_mac_addresses": security_data.get(
            "maximum_mac_addresses"
        ),
        "sticky_mac_addresses": security_data.get(
            "sticky_mac_addresses"
        ),
        "security_violation_count": violation_count,
        "interface_status": interface_status,
        "expected_port_status": expected_data.get(
            "port_status"
        ),
        "expected_interface_status": expected_data.get(
            "interface_status"
        ),
        "explanation": (
            f"{faulty_device} interface {faulty_interface} "
            f"experienced a port security violation. "
            f"The port entered {port_status} state with "
            f"{violation_count} security violation(s), causing "
            f"the interface to become {interface_status}."
        ),
        "recommended_fix": (
            f"Investigate the unauthorized MAC address on "
            f"{faulty_device} {faulty_interface}, remove or update "
            f"the port security configuration if required, then "
            f"recover the interface using 'shutdown' followed by "
            f"'no shutdown'."
        )
    }