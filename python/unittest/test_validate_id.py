import pytest
import re


def validate_id(id: str) -> bool:
    email_pattern = r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
    match = re.match(email_pattern, id)
    if match:
        return True
    return False


@pytest.mark.parametrize("id, value", [
    ("test@example.com", True),
    ("user123", False),
    ("john.doe@gmail.com", True),
    ("12345", False),
    ("user@example", False),
    ("test123@test.co.uk", True),
    ("user@123.com", True),
    ("john.doe", False),
    ("@example.com", False),
    ("user@example..com", False)
])
def test_validate_id(id: str, value: str) -> bool:
    assert validate_id(id) == value
