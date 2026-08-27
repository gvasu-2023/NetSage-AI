from rules.dns_service_rules import diagnose_dns_service_failure


def test_dns_service_failure_detected():

    case_data = {
        "category": "DNS",

        "topology": {
            "faulty_device": "Server0",
            "dns_client": "PC1",
            "dns_server_ip": "192.168.30.10",
            "hostname": "external-pc.netsage.local",
            "expected_ip_address": "172.16.10.10"
        },

        "dns_service": {
            "service_status": "OFF",
            "configured_dns_server": "192.168.30.10",
            "dns_record_exists": True
        },

        "symptoms": {
            "direct_ip_connectivity": "working",
            "hostname_resolution": "failed"
        }
    }

    result = diagnose_dns_service_failure(case_data)

    assert result["fault_detected"] is True
    assert result["diagnosis"] == "DNS Service Failure"
    assert result["faulty_device"] == "Server0"
    assert result["osi_layer"] == "Layer 7"
    assert result["confidence"] == "High"