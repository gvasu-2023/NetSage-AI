from rules.vlan_rules import diagnose_vlan_assignment


def test_correct_vlan_assignment_is_not_detected():
    """
    A correctly assigned switch port must not be diagnosed
    as a VLAN fault.
    """

    case_data = {
        "device_configs": {
            "SW1": {
                "faulty_interface": "Fa0/2",
                "actual_vlan": 20,
                "expected_vlan": 20
            }
        }
    }

    diagnosis = diagnose_vlan_assignment(case_data)

    assert diagnosis["fault_detected"] is False