from pathlib import Path

from rules.case_loader import load_all_cases
from rules.gateway_rules import diagnose_default_gateway
from rules.vlan_rules import diagnose_vlan_assignment
from rules.dhcp_rules import diagnose_dhcp_service_failure
from rules.interface_rules import diagnose_interface_administratively_down
from rules.routing_rules import diagnose_missing_static_route
from rules.subnet_rules import diagnose_wrong_subnet_mask
from rules.trunk_rules import diagnose_vlan_missing_from_trunk
from rules.dns_rules import diagnose_wrong_dns_server
from rules.acl_rules import diagnose_acl_blocks_traffic
from rules.port_security_rules import diagnose_port_security_violation
from rules.dhcp_relay_rules import diagnose_dhcp_relay_missing
from rules.native_vlan_rules import diagnose_native_vlan_mismatch

def run_diagnosis_rules(case_data):
    """
    Run all available diagnostic rules.

    New diagnostic rule modules can be added here.
    """

    rules = [
        diagnose_default_gateway,
        diagnose_vlan_assignment,
        diagnose_vlan_missing_from_trunk,
        diagnose_dhcp_service_failure,
        diagnose_dhcp_relay_missing,
        diagnose_interface_administratively_down,
        diagnose_missing_static_route,
        diagnose_wrong_subnet_mask,
        diagnose_wrong_dns_server,
        diagnose_acl_blocks_traffic,
        diagnose_port_security_violation,
        diagnose_native_vlan_mismatch
    ]

    for rule in rules:
        diagnosis = rule(case_data)

        if diagnosis.get("fault_detected"):
            return diagnosis

    return {
        "fault_detected": False,
        "diagnosis": "Unknown Fault",
        "confidence": "Low",
        "explanation": "No available rule matched the case data."
    }


def print_diagnosis(case_data, diagnosis):
    """
    Print a readable diagnosis report.
    """

    print("\n" + "=" * 60)
    print("NETSAGE AI - NETWORK DIAGNOSIS REPORT")
    print("=" * 60)

    print(f"Case ID: {case_data.get('case_id')}")
    print(f"Title: {case_data.get('title')}")

    print("-" * 60)

    if diagnosis.get("fault_detected"):

        print("Fault Detected: YES")
        print(f"Category: {diagnosis.get('category')}")
        print(f"Diagnosis: {diagnosis.get('diagnosis')}")
        print(f"Faulty Device: {diagnosis.get('faulty_device')}")

        if diagnosis.get("faulty_interface"):
            print(
                "Faulty Interface: "
                f"{diagnosis.get('faulty_interface')}"
            )

        print(f"OSI Layer: {diagnosis.get('osi_layer')}")
        print(f"Confidence: {diagnosis.get('confidence')}")

        # Gateway-specific details

        if diagnosis.get("configured_gateway"):
            print(
                "Configured Gateway: "
                f"{diagnosis.get('configured_gateway')}"
            )

        if diagnosis.get("expected_gateway"):
            print(
                "Expected Gateway: "
                f"{diagnosis.get('expected_gateway')}"
            )

        # VLAN-specific details

        if diagnosis.get("actual_vlan") is not None:
            print(
                "Actual VLAN: "
                f"{diagnosis.get('actual_vlan')}"
            )

        if diagnosis.get("expected_vlan") is not None:
            print(
                "Expected VLAN: "
                f"{diagnosis.get('expected_vlan')}"
            )

        # Interface-specific details

        if diagnosis.get("interface_status"):
            print(
                "Interface Status: "
                f"{diagnosis.get('interface_status')}"
            )

        if diagnosis.get("expected_status"):
            print(
                "Expected Status: "
                f"{diagnosis.get('expected_status')}"
            )

        # DHCP-specific details

        if "dhcp_service_enabled" in diagnosis:

            service_status = (
                "ON"
                if diagnosis.get("dhcp_service_enabled")
                else "OFF"
            )

            print(
                f"DHCP Service: {service_status}"
            )

        if diagnosis.get("dhcp_client_ip_address"):
            print(
                "DHCP Client IP Address: "
                f"{diagnosis.get('dhcp_client_ip_address')}"
            )

        if diagnosis.get("expected_network"):
            print(
                "Expected Network: "
                f"{diagnosis.get('expected_network')}"
            )

        # Static route-specific details

        if diagnosis.get("destination_network"):
            print(
                "Destination Network: "
                f"{diagnosis.get('destination_network')}"
            )

        if diagnosis.get("subnet_mask"):
            print(
                "Subnet Mask: "
                f"{diagnosis.get('subnet_mask')}"
            )

        if diagnosis.get("next_hop"):
            print(
                "Expected Next Hop: "
                f"{diagnosis.get('next_hop')}"
            )

        # Subnet mask-specific details

        if diagnosis.get("configured_subnet_mask"):
            print(
                "Configured Subnet Mask: "
                f"{diagnosis.get('configured_subnet_mask')}"
            )

        if diagnosis.get("expected_subnet_mask"):
            print(
                "Expected Subnet Mask: "
                f"{diagnosis.get('expected_subnet_mask')}"
            )

        # Trunk-specific details

        if diagnosis.get("missing_vlan") is not None:
            print(
                "Missing VLAN: "
                f"{diagnosis.get('missing_vlan')}"
            )

        if diagnosis.get("actual_allowed_vlans") is not None:
            print(
                "Allowed VLANs: "
                f"{diagnosis.get('actual_allowed_vlans')}"
            )

        # DNS-specific details

        if diagnosis.get("configured_dns_server"):
            print(
                "Configured DNS Server: "
                f"{diagnosis.get('configured_dns_server')}"
            )

        if diagnosis.get("correct_dns_server"):
            print(
                "Correct DNS Server: "
                f"{diagnosis.get('correct_dns_server')}"
            )

        if diagnosis.get("hostname"):
            print(
                "Hostname: "
                f"{diagnosis.get('hostname')}"
            )

        if diagnosis.get("expected_ip_address"):
            print(
                "Expected IP Address: "
                f"{diagnosis.get('expected_ip_address')}"
            )

        # ACL-specific details

        if diagnosis.get("acl_number") is not None:
            print(
                "ACL Number: "
                f"{diagnosis.get('acl_number')}"
            )

        if diagnosis.get("acl_direction"):
            print(
                "ACL Direction: "
                f"{diagnosis.get('acl_direction')}"
            )

        if diagnosis.get("blocked_source"):
            print(
                "Blocked Source: "
                f"{diagnosis.get('blocked_source')}"
            )

        if diagnosis.get("blocked_destination"):
            print(
                "Blocked Destination: "
                f"{diagnosis.get('blocked_destination')}"
            )

        # Port security-specific details

        if diagnosis.get("port_status"):
            print(
                "Port Security Status: "
                f"{diagnosis.get('port_status')}"
            )

        if diagnosis.get("violation_mode"):
            print(
                "Violation Mode: "
                f"{diagnosis.get('violation_mode')}"
            )

        if diagnosis.get("maximum_mac_addresses") is not None:
            print(
                "Maximum MAC Addresses: "
                f"{diagnosis.get('maximum_mac_addresses')}"
            )

        if diagnosis.get("security_violation_count") is not None:
            print(
                "Security Violation Count: "
                f"{diagnosis.get('security_violation_count')}"
            )
                # DHCP relay-specific details

        if diagnosis.get("client_device"):
            print(
                "DHCP Client: "
                f"{diagnosis.get('client_device')}"
            )

        if diagnosis.get("dhcp_server"):
            print(
                "DHCP Server: "
                f"{diagnosis.get('dhcp_server')}"
            )

        if diagnosis.get("dhcp_server_ip"):
            print(
                "DHCP Server IP: "
                f"{diagnosis.get('dhcp_server_ip')}"
            )

        if "helper_address_configured" in diagnosis:

            helper_status = (
                "YES"
                if diagnosis.get(
                    "helper_address_configured"
                )
                else "NO"
            )

            print(
                "Helper Address Configured: "
                f"{helper_status}"
            )

        if diagnosis.get("expected_helper_address"):
            print(
                "Expected Helper Address: "
                f"{diagnosis.get('expected_helper_address')}"
            )

        if diagnosis.get("client_ip_address"):
            print(
                "Client IP Address: "
                f"{diagnosis.get('client_ip_address')}"
            )

        if "apipa_assigned" in diagnosis:

            apipa_status = (
                "YES"
                if diagnosis.get("apipa_assigned")
                else "NO"
            )

            print(
                f"APIPA Assigned: {apipa_status}"
            )
                # Native VLAN-specific details

        if diagnosis.get("local_native_vlan") is not None:
            print(
                "Local Native VLAN: "
                f"{diagnosis.get('local_native_vlan')}"
            )

        if diagnosis.get("remote_native_vlan") is not None:
            print(
                "Remote Native VLAN: "
                f"{diagnosis.get('remote_native_vlan')}"
            )

        if diagnosis.get("affected_vlan") is not None:
            print(
                "Affected VLAN: "
                f"{diagnosis.get('affected_vlan')}"
            )
        print("\nExplanation:")
        print(diagnosis.get("explanation"))

        print("\nRecommended Fix:")
        print(diagnosis.get("recommended_fix"))

    else:

        print("Fault Detected: NO")
        print(f"Diagnosis: {diagnosis.get('diagnosis')}")
        print(f"Confidence: {diagnosis.get('confidence')}")

        print("\nExplanation:")
        print(diagnosis.get("explanation"))

    print("=" * 60)


def main():
    """
    Load and diagnose all available troubleshooting cases.
    """

    project_root = Path(__file__).resolve().parent.parent

    cases_directory = (
        project_root
        / "data"
        / "cases"
    )

    cases = load_all_cases(cases_directory)

    print(f"\nLoaded {len(cases)} case(s).")

    for case in cases:

        case_data = case["data"]

        diagnosis = run_diagnosis_rules(case_data)

        print_diagnosis(
            case_data,
            diagnosis
        )


if __name__ == "__main__":
    main()