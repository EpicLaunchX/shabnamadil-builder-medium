import marshmallow
import pytest

from pytemplate.domain.factory import burger_factory
from pytemplate.domain.validators import BurgerSchema


def test_valid_data():
    data = {"bread": "Whole meat", "patty": "Chicken"}
    validated_data = BurgerSchema().load(data)
    result = burger_factory(data)
    if result != validated_data:
        pytest.fails(f"Test failed because the result was {result}, expected {validated_data}")
    assert result == validated_data


def test_missing_bread():
    data = {"patty": "Chicken"}
    with pytest.raises(marshmallow.ValidationError) as e:
        BurgerSchema().load(data)
    assert "bread" in e.value.messages


def test_missing_patty():
    data = {"bread": "Whole meat"}
    with pytest.raises(marshmallow.ValidationError) as e:
        BurgerSchema().load(data)
    assert "patty" in e.value.messages


def test_invalid_bread_data():
    data = {"bread": 5, "patty": "Chicken"}
    try:
        BurgerSchema().load(data)
        assert False
    except marshmallow.ValidationError as e:
        assert "bread" in e.messages


def test_invalid_patty_data():
    data = {"bread": "Whole meat", "patty": 5}
    try:
        BurgerSchema().load(data)
        assert False
    except marshmallow.ValidationError as e:
        assert "patty" in e.messages


def test_invalid_sauce_data():
    data = {"bread": "Whole meat", "patty": "Chicken", "sauce": 5}
    try:
        BurgerSchema().load(data)
        assert False
    except marshmallow.ValidationError as e:
        assert "sauce" in e.messages


def test_empty_bread_field():
    data = {"bread": "", "patty": "Chicken"}
    try:
        BurgerSchema().load(data)
        assert False
    except marshmallow.ValidationError as e:
        assert "bread" in e.messages


def test_empty_patty_field():
    data = {"bread": "Whole meat", "patty": ""}
    try:
        BurgerSchema().load(data)
        assert False
    except marshmallow.ValidationError as e:
        assert "patty" in e.messages


def test_bread_none():
    data = {"bread": None, "patty": "Chicken"}
    try:
        BurgerSchema().load(data)
        assert False
    except marshmallow.ValidationError as e:
        assert "bread" in e.messages


def test_patty_none():
    data = {"bread": "Whole meat", "patty": None}
    try:
        BurgerSchema().load(data)
        assert False
    except marshmallow.ValidationError as e:
        assert "patty" in e.messages


def test_valid_toppings():
    data = {"bread": "Whole wheat", "patty": "Beef", "toppings": ["Lettuce", "Tomato", "Onion"]}
    try:
        validated_data = BurgerSchema().load(data)
        result = burger_factory(data)
        assert result == validated_data
    except marshmallow.ValidationError as e:
        assert False, f"Unexpected validation error: {e}"


def test_invalid_toppings_not_a_list():
    data = {"bread": "Whole wheat", "patty": "Beef", "toppings": "Lettuce"}
    try:
        BurgerSchema().load(data)
        assert False
    except marshmallow.ValidationError as e:
        assert "toppings" in e.messages


def test_invalid_toppings_with_non_string_elements():
    data = {"bread": "Whole wheat", "patty": "Beef", "toppings": ["Lettuce", 123]}
    try:
        BurgerSchema().load(data)
        assert False
    except marshmallow.ValidationError as e:
        assert "toppings" in e.messages


def test_empty_toppings():
    data = {"bread": "Whole wheat", "patty": "Beef", "toppings": []}
    try:
        validated_data = BurgerSchema().load(data)
        result = burger_factory(data)
        assert result == validated_data
    except marshmallow.ValidationError as e:
        assert False, f"Unexpected validation error: {e}"


def test_bread_false():
    data = {"bread": False, "patty": "Beef", "sauce": "BBQ"}
    try:
        BurgerSchema().load(data)
        assert False
    except marshmallow.ValidationError as e:
        assert "bread" in e.messages


def test_patty_false():
    data = {"bread": "Whole wheat", "patty": False, "sauce": "BBQ"}
    try:
        BurgerSchema().load(data)
        assert False
    except marshmallow.ValidationError as e:
        assert "patty" in e.messages


def test_sauce_false():
    data = {"bread": "Whole wheat", "patty": "Beef", "sauce": False}
    try:
        BurgerSchema().load(data)
        assert False
    except marshmallow.ValidationError as e:
        assert "sauce" in e.messages


def test_toppings_false():
    data = {"bread": "Whole wheat", "patty": "Beef", "toppings": False}
    try:
        BurgerSchema().load(data)
        assert False
    except marshmallow.ValidationError as e:
        assert "toppings" in e.messages


def test_toppings_contain_false():
    data = {"bread": "Whole wheat", "patty": "Beef", "toppings": ["Lettuce", False]}
    try:
        BurgerSchema().load(data)
        assert False
    except marshmallow.ValidationError as e:
        assert "toppings" in e.messages
