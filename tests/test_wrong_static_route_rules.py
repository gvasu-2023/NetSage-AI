from rules.wrong_static_route_rules import (
    diagnose_wrong_static_route_next_hop
)


def test_wrong_static_route_next_hop_detected():

    case_data = {
        "case_id": "CASE014",
        "title": "Wrong Static Route Next Hop",
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
            "configured_next_hop": "10.0.0.6",
            "expected_next_hop": "10.0.0.2",
            "next_hop_reachable": False,
            "route_installed": False
        },

        "symptoms": {
            "destination_ping": "failed",
            "local_gateway_ping": "successful"
        }
    }

    result = diagnose_wrong_static_route_next_hop(
        case_data
    )

    assert result["fault_detected"] is True
    assert result["category"] == "Routing"
    assert result["diagnosis"] == (
        "Wrong Static Route Next Hop"
    )
    assert result["configured_next_hop"] == "10.0.0.6"
    assert result["expected_next_hop"] == "10.0.0.2"
    assert result["route_installed"] is False
    assert result["osi_layer"] == "Layer 3"
    assert result["confidence"] == "High"