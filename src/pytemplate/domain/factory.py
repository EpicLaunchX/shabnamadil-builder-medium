import marshmallow

from pytemplate.domain.models import Burger
from pytemplate.domain.validators import BurgerSchema


def burger_factory(data):
    try:
        validated_data = BurgerSchema().load(data)
        return Burger(**validated_data)
    except marshmallow.ValidationError as err:
        return err.messages
