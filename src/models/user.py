class User:
    def __init__(self, first_name, last_name, email, phone_number, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.password = password

    def __str__(self):
        return f"""
            First Name: {self.first_name}
            Last Name: {self.last_name}
            Email: {self.email}
            Phone Number: {self.phone_number}
            Password: {self.password}
            """
