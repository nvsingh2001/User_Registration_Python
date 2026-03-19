import re

def get_input(field, pattern, error):
    while True:
        try:
            value = input(f"Enter {field} :")
            if not re.match(pattern, value):
                raise ValueError(f"Error: {error}")
            return value
        except ValueError as e:
            print(e)
