from src.models.user import User


def test_user_creation():
    user = User("John", "Doe", "john@example.com", "91 9876543210", "Pass@123")
    assert user.first_name == "John"
    assert user.last_name == "Doe"
    assert user.email == "john@example.com"
    assert user.phone_number == "91 9876543210"
    assert user.password == "Pass@123"


def test_user_str():
    user = User("John", "Doe", "john@example.com", "91 9876543210", "Pass@123")
    str_repr = str(user)
    assert "John" in str_repr
    assert "john@example.com" in str_repr
