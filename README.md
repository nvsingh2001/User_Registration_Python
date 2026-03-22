# User Registration System

A robust Python-based User Registration System that ensures data integrity through precise regular expression validation. This project demonstrates modular design, custom input handling, and rigorous validation for user profile fields.

## 🚀 Features

- **Input Validation**: Real-time validation for all registration fields.
- **Custom Error Handling**: Detailed error messages for invalid inputs.
- **Modular Architecture**: Clean separation of models, utilities, and main logic.
- **Comprehensive Testing**: Full test suite for models, validation, and input handling.

## 🛠️ Field Validation Rules

The system enforces the following rules for user registration:

| Field | Validation Rule |
| :--- | :--- |
| **First Name** | Must start with a Capital letter and have a minimum of 3 characters. |
| **Last Name** | Must start with a Capital letter and have a minimum of 3 characters. |
| **Email** | Validates standard email formats (e.g., `username@domain.extension`). Supports sub-domains and special characters in the username. |
| **Phone Number** | Format: `CountryCode PhoneDigits` (e.g., `91 9876543210`). |
| **Password** | - Minimum 8 characters<br>- At least one uppercase letter<br>- At least one numeric character<br>- **Exactly one** special character |

## 📁 Project Structure

```text
UserRegistration/
├── src/
│   ├── main.py              # Application entry point
│   ├── models/
│   │   └── user.py          # User class definition
│   └── utils/
│       ├── input_handler.py # Handles user interaction and validation loops
│       └── validation.py    # Regex patterns and error messages
├── tests/                   # Pytest test suite
│   ├── test_input_handler.py
│   ├── test_user.py
│   └── test_validation.py
└── README.md
```

## ⚙️ Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd UserRegistration
   ```

2. **Set up a virtual environment** (Recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## 🖥️ Usage

Run the main application using Python:

```bash
python3 src/main.py
```

Follow the on-screen prompts to register a user. The system will continue to ask for valid input if the validation rules are not met.

## 🧪 Running Tests

The project uses `pytest` for unit testing. To execute all tests, run:

```bash
pytest
```

To run a specific test file:
```bash
pytest tests/test_validation.py
```

## 📝 License

This project is for educational purposes as part of the BridgeLabz training program.
