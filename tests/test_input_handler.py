from src.utils.input_handler import get_input
from src.utils.validation import NAME_PATTERN, NAME_ERROR


def test_get_input_retry_logic(monkeypatch):
    inputs = iter(["jo", "John"])
    printed = []

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    monkeypatch.setattr("builtins.print", lambda *args, **kwargs: printed.append(args))

    result = get_input("First Name", NAME_PATTERN, NAME_ERROR)

    assert result == "John"
    assert len(printed) == 1
    assert NAME_ERROR in str(printed[0])
