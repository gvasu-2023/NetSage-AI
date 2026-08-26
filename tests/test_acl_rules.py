from rules.acl_rules import diagnose_acl_blocks_traffic


def test_acl_blocks_traffic_detected():

    case_data = {
        "case_id": "CASE009",
        "title": "ACL Blocks Traffic",
        "category": "ACL",

        "topology": {
            "faulty_device": "R1",
            "faulty_interface": "GigabitEthernet0/1",
            "source_ip": "192.168.10.10",
            "destination_ip": "172.16.10.10"
        },

        "acl": {
            "acl_number": 101,
            "direction": "out",
            "interface": "GigabitEthernet0/1",
            "action": "deny",
            "protocol": "ip",
            "source": "192.168.10.10",
            "destination": "172.16.10.10",
            "permit_other_traffic": True
        }
    }

    result = diagnose_acl_blocks_traffic(case_data)

    assert result["fault_detected"] is True
    assert result["category"] == "ACL"
    assert result["diagnosis"] == "ACL Blocks Traffic"
    assert result["faulty_device"] == "R1"
    assert result["faulty_interface"] == "GigabitEthernet0/1"
    assert result["acl_number"] == 101
    assert result["acl_direction"] == "out"
    assert result["blocked_source"] == "192.168.10.10"
    assert result["blocked_destination"] == "172.16.10.10"
    assert result["osi_layer"] == "Layer 3"
    assert result["confidence"] == "High"