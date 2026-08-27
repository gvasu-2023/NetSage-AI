from rules.native_vlan_rules import (
    diagnose_native_vlan_mismatch
)


def test_native_vlan_mismatch_detected():

    case_data = {
        "case_id": "CASE012",
        "title": "Native VLAN Mismatch",
        "category": "VLAN",

        "topology": {
            "faulty_device": "SW1",
            "faulty_interface": "GigabitEthernet0/1",
            "connected_device": "R1",
            "connected_interface": "GigabitEthernet0/0",
            "affected_vlan": 10
        },

        "native_vlan": {
            "local_native_vlan": 10,
            "remote_native_vlan": 1,
            "mismatch_detected": True
        },

        "symptoms": {
            "affected_vlan_gateway_ping": "failed",
            "affected_vlan_remote_ping": "failed",
            "other_vlans_connectivity": "working"
        }
    }

    result = diagnose_native_vlan_mismatch(case_data)

    assert result["fault_detected"] is True
    assert result["category"] == "VLAN"
    assert result["diagnosis"] == "Native VLAN Mismatch"
    assert result["faulty_device"] == "SW1"
    assert result["faulty_interface"] == "GigabitEthernet0/1"
    assert result["connected_device"] == "R1"
    assert result["connected_interface"] == "GigabitEthernet0/0"
    assert result["affected_vlan"] == 10
    assert result["local_native_vlan"] == 10
    assert result["remote_native_vlan"] == 1
    assert result["osi_layer"] == "Layer 2"
    assert result["confidence"] == "High"