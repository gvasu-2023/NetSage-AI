from rules.acl_rules import diagnose_acl_blocks_traffic


def test_acl_blocks_traffic_detected():

    case_data = {
        "case_id": "CASE009",
        "title": "ACL Blocking Traffic",
        "category": "ACL",
        "severity": "High",

        "topology": {
            "faulty_device": "R1",
            "source_device": "PC1",
            "destination_device": "External-PC",
            "outgoing_interface": "GigabitEthernet0/1"
        },

        "acl_configuration": {
            "acl_number": "101",
            "acl_direction": "out",
            "blocked_source": "192.168.10.10",
            "blocked_destination": "172.16.10.10",
            "deny_rule_present": True,
            "permit_other_traffic": True
        },

        "symptoms": {
            "source_to_destination_ping": "failed",
            "acl_match": True
        },

        "expected_diagnosis": {
            "category": "ACL",
            "diagnosis": "ACL Blocking Traffic",
            "faulty_device": "R1",
            "faulty_interface": "GigabitEthernet0/1",
            "osi_layer": "Layer 3/4",
            "confidence": "High"
        }
    }

    result = diagnose_acl_blocks_traffic(case_data)

    assert result["fault_detected"] is True
    assert result["category"] == "ACL"
    assert result["diagnosis"] == "ACL Blocking Traffic"
    assert result["faulty_device"] == "R1"
    assert result["faulty_interface"] == "GigabitEthernet0/1"
    assert result["acl_number"] == "101"
    assert result["acl_direction"] == "out"
    assert result["blocked_source"] == "192.168.10.10"
    assert result["blocked_destination"] == "172.16.10.10"
    assert result["osi_layer"] == "Layer 3/4"
    assert result["confidence"] == "High"