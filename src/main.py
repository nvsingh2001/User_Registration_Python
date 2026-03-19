from models.user import User
from utils.validation import (
    NAME_PATTERN,
    NAME_ERROR,
    EMAIL_PATTERN,
    EMAIL_ERROR,
    PHONE_PATTERN,
    PHONE_ERROR,
    PASSWORD_PATTERN,
    PASSWORD_ERROR,
)
from utils.input_handler import get_input


def main():
    first_name = get_input("First Name", NAME_PATTERN, f"First Name {NAME_ERROR}")
    last_name = get_input("Last Name", NAME_PATTERN, f"Last Name {NAME_ERROR}")
    email = get_input("Email", EMAIL_PATTERN, EMAIL_ERROR)
    phone_number = get_input("Phone Number", PHONE_PATTERN, PHONE_ERROR)
    password = get_input("Password", PASSWORD_PATTERN, PASSWORD_ERROR)

    user = User(first_name, last_name, email, phone_number, password)
    print(user)


if __name__ == "__main__":
    main()
