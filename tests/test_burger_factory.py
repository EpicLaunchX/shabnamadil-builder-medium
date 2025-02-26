import marshmallow
import pytest

from pytemplate.domain.models import Burger, burger_factory
from pytemplate.domain.validators import BurgerSchema


def test_valid_data():
    data = {"bread": "Whole meat", "patty": "Chicken"}

    try:
        validated_data = BurgerSchema().load(data)
    except marshmallow.ValidationError as e:
        pytest.fail(f"Schema validation failed: {e}")

    burger_object = burger_factory(validated_data)

    assert isinstance(burger_object, Burger)
    assert burger_object.bread == data["bread"]
    assert burger_object.patty == data["patty"]


def test_valid_toppings():
    data = {"bread": "Whole wheat", "patty": "Beef", "sauce": "BBQ", "toppings": ["Lettuce", "Tomato", "Onion"]}
    try:
        validated_data = BurgerSchema().load(data)
    except marshmallow.ValidationError as e:
        pytest.fail(f"Schema validation failed: {e}")

    burger_object = burger_factory(validated_data)
    assert isinstance(burger_object, Burger)


def test_missing_bread():
    data = {"patty": "Chicken"}
    with pytest.raises(marshmallow.ValidationError):
        burger_factory(data)


def test_missing_patty():
    data = {"bread": "Whole meat"}
    with pytest.raises(marshmallow.ValidationError):
        burger_factory(data)
