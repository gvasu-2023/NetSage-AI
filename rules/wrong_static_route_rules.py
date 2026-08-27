def diagnose_wrong_static_route_next_hop(case_data):
    """
    Diagnose a static route configured with an incorrect next hop.
    """

    if case_data.get("category") != "Routing":
        return {
            "fault_detected": False
        }

    topology = case_data.get("topology", {})
    routing = case_data.get("routing", {})
    symptoms = case_data.get("symptoms", {})

    route_configured = routing.get(
        "route_configured",
        False
    )

    configured_next_hop = routing.get(
        "configured_next_hop"
    )

    expected_next_hop = routing.get(
        "expected_next_hop"
    )

    next_hop_reachable = routing.get(
        "next_hop_reachable",
        True
    )

    route_installed = routing.get(
        "route_installed",
        True
    )

    destination_ping_failed = (
        symptoms.get("destination_ping") == "failed"
    )

    local_gateway_ping_successful = (
        symptoms.get("local_gateway_ping") == "successful"
    )

    wrong_next_hop = (
        route_configured
        and configured_next_hop is not None
        and expected_next_hop is not None
        and configured_next_hop != expected_next_hop
    )

    if (
        not wrong_next_hop
        or next_hop_reachable
        or route_installed
        or not destination_ping_failed
        or not local_gateway_ping_successful
    ):
        return {
            "fault_detected": False
        }

    faulty_device = topology.get("faulty_device")
    faulty_interface = topology.get("faulty_interface")
    destination_network = topology.get(
        "destination_network"
    )
    destination_ip = topology.get(
        "destination_ip"
    )

    return {
        "fault_detected": True,
        "category": "Routing",
        "diagnosis": "Wrong Static Route Next Hop",
        "faulty_device": faulty_device,
        "faulty_interface": faulty_interface,
        "destination_device": topology.get(
            "destination_device"
        ),
        "destination_network": destination_network,
        "destination_ip": destination_ip,
        "configured_next_hop": configured_next_hop,
        "expected_next_hop": expected_next_hop,
        "next_hop_reachable": next_hop_reachable,
        "route_installed": route_installed,
        "osi_layer": "Layer 3",
        "confidence": "High",
        "explanation": (
            f"{faulty_device} has a static route to "
            f"{destination_network}, but the route uses "
            f"the incorrect next hop {configured_next_hop} "
            f"instead of {expected_next_hop}. "
            f"The configured next hop is unreachable, so "
            f"the route is not installed in the routing table. "
            f"As a result, traffic to {destination_ip} fails."
        ),
        "recommended_fix": (
            f"Remove the incorrect static route and configure "
            f"the correct next hop on {faulty_device}: "
            f"'no ip route {destination_network} "
            f"{configured_next_hop}', then configure the route "
            f"using next hop {expected_next_hop}."
        )
    }