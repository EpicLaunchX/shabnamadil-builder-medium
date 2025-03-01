from unittest import mock

import pytest
from marshmallow import ValidationError

from pytemplate.domain.models import Burger
from pytemplate.entrypoints.cli.main import main
from pytemplate.utils.common import get_choice_input


@pytest.mark.parametrize(
    "mock_input, expected_output",
    [
        (
            "chicken",
            Burger(bread="Sesame Seed Bun", patty="Chicken", sauce="Ketchup", toppings=["Lettuce", "Tomato"]),
        ),
        ("cheese", Burger(bread="Sesame Seed Bun", patty="Chicken", sauce="Ketchup", toppings=["Lettuce", "Tomato"])),
        ("vegan", Burger(bread="Sesame Seed Bun", patty="Chicken", sauce="Ketchup", toppings=["Lettuce", "Tomato"])),
    ],
)
def test_main_valid_inputs(mock_input, expected_output):
    with mock.patch("builtins.input", side_effect=[mock_input]):
        assert main() == expected_output


@pytest.mark.parametrize(
    "mock_input, expected_exception, error_message",
    [
        ("invalid", ValidationError, "Invalid choice!"),
        ("", ValidationError, "Invalid choice!"),
        (None, ValidationError, "Invalid choice!"),
        (123, ValidationError, "Invalid choice!"),
    ],
)
def test_main_invalid_inputs(mock_input, expected_exception, error_message):
    with mock.patch("builtins.input", side_effect=[mock_input]):
        with pytest.raises(expected_exception, match=error_message):
            main()


@pytest.mark.parametrize("interrupt_exception", [EOFError, KeyboardInterrupt])
def test_get_choice_input_interrupted(interrupt_exception):
    with mock.patch("builtins.input", side_effect=interrupt_exception):
        with pytest.raises(ValidationError, match="Input was interrupted. Please try again."):
            get_choice_input()
