import pytest
from marshmallow import ValidationError

from pytemplate.domain.validators import BurgerSchema


def test_valid_data():
    data = {"bread": "Whole meat", "patty": "Chicken"}

    # Test deserialization (load)
    result = BurgerSchema().load(data)
    assert result["bread"] == "Whole meat"
    assert result["patty"] == "Chicken"

    # Test serialization (dump)
    serialized_data = BurgerSchema().dump(result)
    assert serialized_data["bread"] == "Whole meat"
    assert serialized_data["patty"] == "Chicken"


def test_missing_bread():
    data = {"patty": "Chicken"}
    with pytest.raises(ValidationError):
        BurgerSchema().load(data)


def test_missing_patty():
    data = {"bread": "Whole meat"}
    with pytest.raises(ValidationError):
        BurgerSchema().load(data)


def test_invalid_bread_data():
    data = {"bread": 5, "patty": "Chicken"}
    with pytest.raises(ValidationError):
        BurgerSchema().load(data)


def test_invalid_patty_data():
    data = {"bread": "Whole meat", "patty": 5}
    with pytest.raises(ValidationError):
        BurgerSchema().load(data)


def test_missing_both_fields():
    data = {}
    with pytest.raises(ValidationError):
        BurgerSchema().load(data)


def test_empty_bread_field():
    data = {"bread": "", "patty": "Chicken"}
    with pytest.raises(ValidationError):
        BurgerSchema().load(data)


def test_empty_patty_field():
    data = {"bread": "Whole meat", "patty": ""}
    with pytest.raises(ValidationError):
        BurgerSchema().load(data)


def test_bread_none():
    data = {"bread": None, "patty": "Chicken"}
    with pytest.raises(ValidationError):
        BurgerSchema().load(data)


def test_patty_none():
    data = {"bread": "Whole meat", "patty": None}
    with pytest.raises(ValidationError):
        BurgerSchema().load(data)


def test_valid_toppings():
    """Ensure valid toppings list works"""
    data = {"bread": "Whole wheat", "patty": "Beef", "toppings": ["Lettuce", "Tomato", "Onion"]}
    result = BurgerSchema().load(data)
    assert result["toppings"] == ["Lettuce", "Tomato", "Onion"]


def test_invalid_toppings_not_a_list():
    """Ensure toppings must be a list"""
    data = {"bread": "Whole wheat", "patty": "Beef", "toppings": "Lettuce"}
    with pytest.raises(ValidationError):
        BurgerSchema().load(data)


def test_invalid_toppings_with_non_string_elements():
    """Ensure toppings must contain only strings"""
    data = {"bread": "Whole wheat", "patty": "Beef", "toppings": ["Lettuce", 123]}
    with pytest.raises(ValidationError):
        BurgerSchema().load(data)


def test_empty_toppings():
    """Ensure empty toppings list is allowed"""
    data = {"bread": "Whole wheat", "patty": "Beef", "toppings": []}
    result = BurgerSchema().load(data)
    assert result["toppings"] == []


def test_valid_sauce():
    """Ensure valid sauce field is allowed"""
    data = {"bread": "Whole wheat", "patty": "Beef", "sauce": "Mayo"}
    result = BurgerSchema().load(data)
    assert result["sauce"] == "Mayo"


def test_invalid_sauce():
    """Ensure sauce must be a string"""
    data = {"bread": "Whole wheat", "patty": "Beef", "sauce": 123}
    with pytest.raises(ValidationError):
        BurgerSchema().load(data)


def test_valid_toppings_and_sauce():
    """Ensure toppings and sauce can be valid together"""
    data = {"bread": "Whole wheat", "patty": "Beef", "sauce": "BBQ", "toppings": ["Cheese", "Pickles"]}
    result = BurgerSchema().load(data)
    assert result["sauce"] == "BBQ"
    assert result["toppings"] == ["Cheese", "Pickles"]


def test_bread_false():
    """Ensure False as bread is rejected"""
    data = {"bread": False, "patty": "Beef"}
    with pytest.raises(ValidationError):
        BurgerSchema().load(data)


def test_patty_false():
    """Ensure False as patty is rejected"""
    data = {"bread": "Whole wheat", "patty": False}
    with pytest.raises(ValidationError):
        BurgerSchema().load(data)


def test_sauce_false():
    """Ensure False as sauce is rejected"""
    data = {"bread": "Whole wheat", "patty": "Beef", "sauce": False}
    with pytest.raises(ValidationError):
        BurgerSchema().load(data)


def test_toppings_false():
    """Ensure False as toppings is rejected"""
    data = {"bread": "Whole wheat", "patty": "Beef", "toppings": False}
    with pytest.raises(ValidationError):
        BurgerSchema().load(data)


def test_toppings_contain_false():
    """Ensure toppings list containing False is rejected"""
    data = {"bread": "Whole wheat", "patty": "Beef", "toppings": ["Lettuce", False]}
    with pytest.raises(ValidationError):
        BurgerSchema().load(data)
