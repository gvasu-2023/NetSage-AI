from rules.dns_rules import diagnose_wrong_dns_server


def test_detect_wrong_dns_server():

    case_data = {
        "case_id": "CASE008",
        "topology": {
            "faulty_device": "PC1"
        },
        "ip_configuration": {
            "configured_dns_server": "192.168.10.254"
        },
        "expected_state": {
            "correct_dns_server": "192.168.30.10",
            "hostname": "external-pc.netsage.local",
            "expected_ip_address": "172.16.10.10"
        },
        "symptoms": {
            "hostname_resolution": "failed",
            "direct_ip_connectivity": "working"
        }
    }

    diagnosis = diagnose_wrong_dns_server(case_data)

    assert diagnosis["fault_detected"] is True
    assert diagnosis["category"] == "DNS"
    assert diagnosis["diagnosis"] == "Wrong DNS Server"
    assert diagnosis["faulty_device"] == "PC1"
    assert diagnosis["configured_dns_server"] == "192.168.10.254"
    assert diagnosis["correct_dns_server"] == "192.168.30.10"
    assert diagnosis["confidence"] == "High"