import re
import pytest

def inpect_url(address: str) -> bool:
    url_pattern = r"^https?:\/\/(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b(?:[-a-zA-Z0-9()@:%_\+.~#?&\/=]*)$"
    match = re.match(url_pattern, address)
    if match:
        return True
    return False

@pytest.mark.parametrize("address, value", [
    ("https://3451-211-106-17-178.ngrok-free.app/api", True),
    ("https://www.google.co.kr", True),
    ("invalidaddress", False),
    ("ftp://example.com", False),
    ("www.example.com", False),
    ("https://example_com", False),
    ("https://", False),
    ("https://example.com?param1=value1&param2=value2", True),
    ("https://example.com#section", True),
    ("https://192.168.0.1", True),
    ("https://[2001:db8:0:1]:8080", True),  # TODO: 테스트 케이스 통과 못함 [ ] 처리 필요
])
def test_inspect_url_value(address: str, value: bool):
    assert inpect_url(address) == value