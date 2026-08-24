import json
from pathlib import Path


def load_case(case_path):
    """
    Load one troubleshooting case from a JSON file.
    """
    case_path = Path(case_path)

    with case_path.open("r", encoding="utf-8") as file:
        return json.load(file)


def load_all_cases(cases_directory):
    """
    Load all case.json files from the cases directory.
    """
    cases_directory = Path(cases_directory)

    case_files = sorted(
        cases_directory.glob("**/case.json")
    )

    cases = []

    for case_file in case_files:
        case_data = load_case(case_file)

        cases.append(
            {
                "path": str(case_file),
                "data": case_data
            }
        )

    return cases