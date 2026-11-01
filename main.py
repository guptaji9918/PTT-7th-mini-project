import os
import json
from record_utils import validate_student, StudentRecordError
from import_utils import import_records, write_outputs

DEFAULT_INPUT = "students_input.json"
VALID_OUTPUT = "students_valid.json"
ERROR_LOG = "import_errors.txt"

def main():
    input_path = input(f"Input JSON path (blank for {DEFAULT_INPUT}): ").strip() or DEFAULT_INPUT
    print(f"Import started: {input_path}")

    try:
        records = import_records(input_path)
    except FileNotFoundError:
        print(f"Error: input file not found: {input_path}")
        return
    except PermissionError:
        print(f"Error: permission denied: {input_path}")
        return
    except OSError as error:
        print(f"File error: {error}")
        return
    except json.JSONDecodeError as error:
        print(f"JSON parsing error: {error}")
        return
    else:
        accepted, rejected = [], []
        seen_ids = set()
        for index, record in enumerate(records, start=1):
            try:
                student = validate_student(record)
                student_id = student["student_id"]
                if student_id in seen_ids:
                    raise StudentRecordError(f"duplicate student_id '{student_id}'")
                seen_ids.add(student_id)
                accepted.append(student)
                print(f"Accepted: {student_id} - {student['name']}")
            except StudentRecordError as error:
                rejected.append(f"Rejected record {index}: {error}")
            except (TypeError, ValueError, KeyError, IndexError) as error:
                rejected.append(f"Rejected record {index}: invalid data ({error})")

        write_outputs(accepted, rejected, VALID_OUTPUT, ERROR_LOG)
        print("Import completed.")
        print(f"Accepted records: {len(accepted)}")
        print(f"Rejected records: {len(rejected)}")
        print(f"Valid output: {VALID_OUTPUT}")
        print(f"Error log: {ERROR_LOG}")
    finally:
        print("Import process finished.")

if __name__ == "_main_":
    main()