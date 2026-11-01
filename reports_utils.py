class StudentRecordError(Exception):
    """Raised when a student record violates project validation rules."""

def validate_student(record):
    if not isinstance(record, dict):
        raise TypeError("record must be a dictionary")

    required = ("student_id", "name", "department", "marks")
    for field in required:
        if field not in record:
            raise StudentRecordError(f"missing required field '{field}'")

    student_id = record["student_id"]
    name = record["name"]
    department = record["department"]
    marks = record["marks"]

    if not isinstance(student_id, str) or not student_id.strip():
        raise TypeError("student_id must be a non-empty string")
    if not isinstance(name, str) or not name.strip():
        raise TypeError("name must be a non-empty string")
    if not isinstance(department, str) or not department.strip():
        raise TypeError("department must be a non-empty string")
    if not isinstance(marks, list):
        raise TypeError("marks must be a list")
    if len(marks) != 3:
        raise StudentRecordError("marks must contain exactly 3 values between 0 and 100")

    clean_marks = []
    for mark in marks:
        if isinstance(mark, bool) or not isinstance(mark, (int, float)):
            raise StudentRecordError("each mark must be numeric; booleans are not accepted")
        if not 0 <= mark <= 100:
            raise StudentRecordError("marks must contain exactly 3 values between 0 and 100")
        clean_marks.append(mark)

    return {
        "student_id": student_id.strip(),
        "name": name.strip(),
        "department": department.strip(),
        "marks": clean_marks
    }