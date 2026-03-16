import re


class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"""
            First Name: {self.first_name}
            Last Name: {self.last_name}
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
    name_pattern = "^[A-Z][a-z]{2,}$"
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

    user = User(first_name, last_name)

    print(user)


if __name__ == "__main__":
    main()
