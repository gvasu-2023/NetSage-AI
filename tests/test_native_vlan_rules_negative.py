from rules.native_vlan_rules import (
    diagnose_native_vlan_mismatch
)


def test_no_native_vlan_mismatch_detected():

    case_data = {
        "case_id": "TEST012",
        "title": "Healthy Native VLAN Configuration",
        "category": "VLAN",

        "topology": {
            "faulty_device": "SW1",
            "faulty_interface": "GigabitEthernet0/1",
            "connected_device": "R1",
            "connected_interface": "GigabitEthernet0/0",
            "affected_vlan": 10
        },

        "native_vlan": {
            "local_native_vlan": 1,
            "remote_native_vlan": 1,
            "mismatch_detected": False
        },

        "symptoms": {
            "affected_vlan_gateway_ping": "working",
            "affected_vlan_remote_ping": "working",
            "other_vlans_connectivity": "working"
        }
    }

    result = diagnose_native_vlan_mismatch(case_data)

    assert result["fault_detected"] is False