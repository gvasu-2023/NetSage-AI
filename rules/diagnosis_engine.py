from pathlib import Path

from rules.case_loader import load_all_cases

from rules.gateway_rules import diagnose_default_gateway
from rules.vlan_rules import diagnose_vlan_assignment
from rules.dhcp_rules import diagnose_dhcp_service_failure
from rules.interface_rules import diagnose_interface_administratively_down
from rules.routing_rules import diagnose_missing_static_route
def run_diagnosis_rules(case_data):
    """
    Run all available diagnostic rules.

    New diagnostic rule modules can be added here.
    """

    rules = [
        diagnose_default_gateway,
        diagnose_vlan_assignment,
        diagnose_dhcp_service_failure,
        diagnose_interface_administratively_down,
        diagnose_missing_static_route
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
                f"Faulty Interface: "
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
                f"Actual VLAN: "
                f"{diagnosis.get('actual_vlan')}"
            )

        if diagnosis.get("expected_vlan") is not None:
            print(
                f"Expected VLAN: "
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
        print_diagnosis(case_data, diagnosis)


if __name__ == "__main__":
    main()