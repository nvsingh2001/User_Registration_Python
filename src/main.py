import re


class User:
    def __init__(self, first_name, last_name, email, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number

    def __str__(self):
        return f"""
            First Name: {self.first_name}
            Last Name: {self.last_name}
            Email: {self.email}
            Phone Number: {self.phone_number}
            """


def get_input(field, pattern, error):
    while True:
        try:
            value = input(f"Enter {field} :")
            if not re.match(pattern, value):
                raise ValueError(f"Error: {error}")
            return value
        except ValueError as e:
            print(e)


def main():
    name_pattern = r"^[A-Z][a-z]{2,}$"
    email_pattern = r"[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)*@[a-zA-Z0-9]+(\.[a-zA-Z]+)+"
    phone_pattern = r"^[1-9]\d{1,2}\s\d{7,12}$"

    first_name = get_input(
        "First Name",
        name_pattern,
        "First Name should start with capital letter and length should be 3 characters minimum",
    )

    last_name = get_input(
        "Last Name",
        name_pattern,
        "Last Name should start with capital letter and length should be 3 characters minimum",
    )

    email = get_input(
        "Email",
        email_pattern,
        """
            Invalid email format.

            Please enter an email in the format:

            username@domain.extension

            Rules:

            * The username may contain letters and numbers.
            * Dots are allowed in the username but cannot appear at the start, end, or consecutively.
            * The domain may contain at least one dot.
            * Domain extensions must contain letters only.

            Example of valid emails:
            john@example.com
            john.doe123@mail.google.com
        """,
    )

    phone_number = get_input(
        "Phone Number",
        phone_pattern,
        "Invalid phone number format. Please enter a valid phone number.",
    )

    user = User(first_name, last_name, email, phone_number)

    print(user)


if __name__ == "__main__":
    main()
