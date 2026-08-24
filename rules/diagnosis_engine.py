from pathlib import Path

from rules.case_loader import load_all_cases
from rules.gateway_rules import diagnose_default_gateway


def run_diagnosis_rules(case_data):
    """
    Run all available diagnostic rules.

    New diagnostic rule modules can be added here.
    """

    rules = [
        diagnose_default_gateway
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
        print(f"OSI Layer: {diagnosis.get('osi_layer')}")
        print(f"Confidence: {diagnosis.get('confidence')}")

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