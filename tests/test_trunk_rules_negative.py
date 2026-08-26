from rules.trunk_rules import (
    diagnose_vlan_missing_from_trunk
)


def test_required_vlan_present_on_trunk():

    case_data = {
        "topology": {
            "faulty_device": "SW1"
        },
        "trunk": {
            "interface": "Gig0/1",
            "actual_allowed_vlans": [
                1,
                10,
                20,
                30
            ]
        },
        "expected_state": {
            "required_vlan": 20
        }
    }

    diagnosis = diagnose_vlan_missing_from_trunk(
        case_data
    )

    assert diagnosis["fault_detected"] is False