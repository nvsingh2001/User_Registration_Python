# Validation Patterns
NAME_PATTERN = r"^[A-Z][a-z]{2,}$"
EMAIL_PATTERN = r"[a-zA-Z0-9]+([\.+-][a-zA-Z0-9]+)*@[a-zA-Z0-9]+(\.[a-zA-Z]+)+$"
PHONE_PATTERN = r"^[1-9]\d{1,2}\s\d{7,12}$"
PASSWORD_PATTERN = r"^(?=.*[A-Z])(?=.*[0-9])(?=.*[@#$%&^,=+\-!])(?!.*[@#$%&^,=+\-!].*[@#$%&^,=+\-!]).*[\w@#$%&^,=+\-!]{8,}$"

# Error Messages
NAME_ERROR = (
    "should start with capital letter and length should be 3 characters minimum"
)
EMAIL_ERROR = """
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
        """
PHONE_ERROR = "Invalid phone number format. Please enter a valid phone number."
PASSWORD_ERROR = """
        Password should have a atleast 8 characters.
        It should contain atleast one Uppercase letter.
        It should contain atleast one numberic number.
        It should contain exactly one special character.
        """
