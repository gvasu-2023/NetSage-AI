from rules.wrong_static_route_rules import (
    diagnose_wrong_static_route_next_hop
)


def test_healthy_static_route_not_detected_as_fault():

    case_data = {
        "case_id": "HEALTHY014",
        "title": "Healthy Static Route",
        "category": "Routing",

        "topology": {
            "faulty_device": "R1",
            "faulty_interface": "GigabitEthernet0/1",
            "destination_device": "External-PC",
            "destination_ip": "172.16.10.10",
            "destination_network": "172.16.10.0/24"
        },

        "routing": {
            "route_configured": True,
            "configured_next_hop": "10.0.0.2",
            "expected_next_hop": "10.0.0.2",
            "next_hop_reachable": True,
            "route_installed": True
        },

        "symptoms": {
            "destination_ping": "successful",
            "local_gateway_ping": "successful"
        }
    }

    result = diagnose_wrong_static_route_next_hop(
        case_data
    )

    assert result["fault_detected"] is False