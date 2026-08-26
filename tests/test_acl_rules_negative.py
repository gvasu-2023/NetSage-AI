from rules.acl_rules import diagnose_acl_blocks_traffic


def test_no_acl_blocking_detected():

    case_data = {
        "case_id": "TEST001",
        "title": "Healthy ACL Configuration",
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
            "action": "permit",
            "protocol": "ip",
            "source": "192.168.10.10",
            "destination": "172.16.10.10",
            "permit_other_traffic": True
        }
    }

    result = diagnose_acl_blocks_traffic(case_data)

    assert result["fault_detected"] is False