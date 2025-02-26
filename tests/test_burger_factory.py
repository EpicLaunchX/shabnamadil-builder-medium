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


def test_invalid_bread_data():
    data = {"bread": 5, "patty": "Chicken"}
    with pytest.raises(marshmallow.ValidationError):
        burger_factory(data)


def test_invalid_patty_data():
    data = {"bread": "Whole meat", "patty": 5}
    with pytest.raises(marshmallow.ValidationError):
        burger_factory(data)


def test_invalid_sauce_data():
    data = {"bread": "Whole meat", "patty": "Chicken", "sauce": 5}
    with pytest.raises(marshmallow.ValidationError):
        burger_factory(data)


def test_empty_bread_field():
    data = {"bread": "", "patty": "Chicken"}
    with pytest.raises(marshmallow.ValidationError):
        burger_factory(data)


def test_empty_patty_field():
    data = {"bread": "Whole meat", "patty": ""}
    with pytest.raises(marshmallow.ValidationError):
        burger_factory(data)


def test_bread_none():
    data = {"bread": None, "patty": "Chicken"}
    with pytest.raises(marshmallow.ValidationError):
        burger_factory(data)


def test_patty_none():
    data = {"bread": "Whole meat", "patty": None}
    with pytest.raises(marshmallow.ValidationError):
        burger_factory(data)


def test_invalid_toppings_not_a_list():
    data = {"bread": "Whole wheat", "patty": "Beef", "toppings": "Lettuce"}
    with pytest.raises(marshmallow.ValidationError):
        burger_factory(data)


def test_invalid_toppings_with_non_string_elements():
    data = {"bread": "Whole wheat", "patty": "Beef", "toppings": ["Lettuce", 123]}
    with pytest.raises(marshmallow.ValidationError):
        burger_factory(data)


def test_bread_false():
    data = {"bread": False, "patty": "Beef", "sauce": "BBQ"}
    with pytest.raises(marshmallow.ValidationError):
        burger_factory(data)


def test_patty_false():
    data = {"bread": "Whole wheat", "patty": False, "sauce": "BBQ"}
    with pytest.raises(marshmallow.ValidationError):
        burger_factory(data)


def test_sauce_false():
    data = {"bread": "Whole wheat", "patty": "Beef", "sauce": False}
    with pytest.raises(marshmallow.ValidationError):
        burger_factory(data)


def test_toppings_false():
    data = {"bread": "Whole wheat", "patty": "Beef", "toppings": False}
    with pytest.raises(marshmallow.ValidationError):
        burger_factory(data)


def test_toppings_contain_false():
    data = {"bread": "Whole wheat", "patty": "Beef", "toppings": ["Lettuce", False]}
    with pytest.raises(marshmallow.ValidationError):
        burger_factory(data)
