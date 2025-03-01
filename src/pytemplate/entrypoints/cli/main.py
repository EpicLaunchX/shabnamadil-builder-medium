from marshmallow import ValidationError

from pytemplate.utils.common import create_burger, get_choice_input


def main():
    choice = get_choice_input()
    try:
        return create_burger(choice)
    except Exception as err:
        raise ValidationError("An unexpected error occurred while creating the burger.") from err
