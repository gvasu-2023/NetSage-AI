from rules.trunk_rules import (
    diagnose_vlan_missing_from_trunk
)


def test_vlan_missing_from_trunk():

    case_data = {
        "topology": {
            "faulty_device": "SW1"
        },
        "trunk": {
            "interface": "Gig0/1",
            "actual_allowed_vlans": [
                1,
                10,
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

    assert diagnosis["fault_detected"] is True
    assert diagnosis["category"] == "VLAN"
    assert (
        diagnosis["diagnosis"]
        == "VLAN Missing From Trunk"
    )
    assert diagnosis["faulty_device"] == "SW1"
    assert diagnosis["faulty_interface"] == "Gig0/1"
    assert diagnosis["missing_vlan"] == 20
    assert diagnosis["osi_layer"] == "Layer 2"
    assert diagnosis["confidence"] == "High"