"""Common shared file for supplementary utils"""

from marshmallow import ValidationError


def get_choice_input():
    valid_choices = {"chicken", "vegan", "cheese"}
    try:
        choice = input("Please choose a burger type (chicken, vegan, cheese): ").strip().lower()
        if choice not in valid_choices:
            raise ValidationError(f"Invalid choice: {choice}. Please select one of {valid_choices}.")
        return choice
    except (EOFError, KeyboardInterrupt):
        raise ValidationError("Input was interrupted. Please try again.")
