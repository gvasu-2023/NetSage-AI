from rules.dns_service_rules import diagnose_dns_service_failure


def test_dns_service_failure_not_detected_when_dns_is_on():

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
            "service_status": "ON",
            "configured_dns_server": "192.168.30.10",
            "dns_record_exists": True
        },

        "symptoms": {
            "direct_ip_connectivity": "working",
            "hostname_resolution": "working"
        }
    }

    result = diagnose_dns_service_failure(case_data)

    assert result["fault_detected"] is False