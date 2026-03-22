import re
from src.utils import validation


def test_name_valid():
    assert re.match(validation.NAME_PATTERN, "John")
    assert re.match(validation.NAME_PATTERN, "Alice")


def test_name_invalid():
    assert not re.match(validation.NAME_PATTERN, "john")  # No capital
    assert not re.match(validation.NAME_PATTERN, "Jo")  # Too short
    assert not re.match(validation.NAME_PATTERN, "123John")  # Has numbers


def test_email_valid():
    assert re.match(validation.EMAIL_PATTERN, "abc.xyz@bl.co.in")
    assert re.match(validation.EMAIL_PATTERN, "user@domain.com")


def test_email_invalid():
    assert not re.match(validation.EMAIL_PATTERN, "abc@.com")
    assert not re.match(validation.EMAIL_PATTERN, "abc..xyz@domain.com")


def test_phone_valid():
    assert re.match(validation.PHONE_PATTERN, "91 9876543210")


def test_phone_invalid():
    assert not re.match(validation.PHONE_PATTERN, "919876543210")  # No space
    assert not re.match(validation.PHONE_PATTERN, "91 12345")  # Too short


def test_password_valid():
    assert re.match(validation.PASSWORD_PATTERN, "Pass@123")


def test_password_invalid():
    assert not re.match(validation.PASSWORD_PATTERN, "password")  # All lowercase
    assert not re.match(validation.PASSWORD_PATTERN, "Pass@@123")  # Two special chars
    assert not re.match(validation.PASSWORD_PATTERN, "Pass1234")  # No special char
