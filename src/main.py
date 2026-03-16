import re


class User:
    def __init__(self, first_name):
        self.first_name = first_name

    def __str__(self):
        return f"First Name: {self.first_name}"


def get_input(field, pattern, error):
    while True:
        try:
            value = input(f"Enter {field}:")
            if not re.match(pattern, value):
                raise ValueError(f"Error: {error}")
            return value
        except ValueError as e:
            print(e)


def main():
    first_name_pattern = "^[A-Z][a-z]{2,}$"
    first_name = get_input(
        "First Name",
        first_name_pattern,
        "First Name should start with capital letter and length should be 3 characters minimum",
    )

    user = User(first_name)
    print(user)


if __name__ == "__main__":
    main()
