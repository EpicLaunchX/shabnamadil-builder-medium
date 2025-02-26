import pytest
from marshmallow import ValidationError

from pytemplate.domain.validators import BurgerSchema


def test_valid_data():
    data = {"bread": "Whole meat", "patty": "Chicken"}

    # Test deserialization(load)
    result = BurgerSchema().load(data)
    assert result["bread"] == "Whole meat"
    assert result["patty"] == "Chicken"

    # Test serialization(dump)
    serializied_data = BurgerSchema().dump(result)
    assert serializied_data["bread"] == "Whole meat"
    assert serializied_data["patty"] == "Chicken"


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


def test_empy_patty_field():
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
