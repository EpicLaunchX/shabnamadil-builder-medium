import marshmallow

from pytemplate.domain.validators import BurgerSchema


def burger_factory(data):
    try:
        validated_data = BurgerSchema().load(data)
        return validated_data
    except marshmallow.ValidationError as err:
        return err.messages
