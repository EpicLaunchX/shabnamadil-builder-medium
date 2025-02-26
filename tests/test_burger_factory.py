import marshmallow
import pytest

from pytemplate.domain.factory import burger_factory
from pytemplate.domain.validators import BurgerSchema


def test_valid_data():
    data = {"bread": "Whole meat", "patty": "Chicken"}
    validated_data = BurgerSchema().load(data)
    burger_object = burger_factory(validated_data)
    try:
        assert burger_object.bread == data["bread"]
        assert burger_object.patty == data["patty"]
    except Exception as e:
        pytest.raises(marshmallow.ValidationError)


def test_missing_bread():
    data = {"patty": "Chicken"}
    with pytest.raises(marshmallow.ValidationError) as e:
        validated_data = BurgerSchema().load(data)
        burger_factory(validated_data)
    assert "patty" in e.value.messages


# def test_missing_patty():
#     data = {"bread": "Whole meat"}
#     with pytest.raises(marshmallow.ValidationError) as e:
#         BurgerSchema().load(data)
#     if not "patty" in e.value.messages:
#         pytest.fail()
#     assert "patty" in e.value.messages


# def test_invalid_bread_data():
#     data = {"bread": 5, "patty": "Chicken"}
#     with pytest.raises(marshmallow.ValidationError) as e:
#         BurgerSchema().load(data)
#     if not "bread" in e.value.messages:
#         pytest.fail()
#     assert "bread" in e.value.messages


# def test_invalid_patty_data():
#     data = {"bread": "Whole meat", "patty": 5}
#     with pytest.raises(marshmallow.ValidationError) as e:
#         BurgerSchema().load(data)
#     if not "patty" in e.value.messages:
#         pytest.fail()
#     assert "patty" in e.value.messages


# def test_invalid_sauce_data():
#     data = {"bread": "Whole meat", "patty": "Chicken", "sauce": 5}
#     with pytest.raises(marshmallow.ValidationError) as e:
#         BurgerSchema().load(data)
#     if not "sauce" in e.value.messages:
#         pytest.fail()
#     assert "sauce" in e.value.messages


# def test_empty_bread_field():
#     data = {"bread": "", "patty": "Chicken"}
#     with pytest.raises(marshmallow.ValidationError) as e:
#         BurgerSchema().load(data)
#     if not "bread" in e.value.messages:
#         pytest.fail()
#     assert "bread" in e.value.messages


# def test_empty_patty_field():
#     data = {"bread": "Whole meat", "patty": ""}
#     with pytest.raises(marshmallow.ValidationError) as e:
#         BurgerSchema().load(data)
#     if not "patty" in e.value.messages:
#         pytest.fail()
#     assert "patty" in e.value.messages


# def test_bread_none():
#     data = {"bread": None, "patty": "Chicken"}
#     with pytest.raises(marshmallow.ValidationError) as e:
#         BurgerSchema().load(data)
#     if not "bread" in e.value.messages:
#         pytest.fail()
#     assert "bread" in e.value.messages


# def test_patty_none():
#     data = {"bread": "Whole meat", "patty": None}
#     with pytest.raises(marshmallow.ValidationError) as e:
#         BurgerSchema().load(data)
#     if not "patty" in e.value.messages:
#         pytest.fail()
#     assert "patty" in e.value.messages


# def test_valid_toppings():
#     data = {"bread": "Whole wheat", "patty": "Beef", "toppings": ["Lettuce", "Tomato", "Onion"]}
#     try:
#         validated_data = BurgerSchema().load(data)
#     except Exception as e:
#         pytest.fail(f"Schema validation failed with error: {e}")
#     assert validated_data == data


# def test_invalid_toppings_not_a_list():
#     data = {"bread": "Whole wheat", "patty": "Beef", "toppings": "Lettuce"}
#     with pytest.raises(marshmallow.ValidationError) as e:
#         BurgerSchema().load(data)
#     if not "toppings" in e.value.messages:
#         pytest.fail()
#     assert "toppings" in e.value.messages


# def test_invalid_toppings_with_non_string_elements():
#     data = {"bread": "Whole wheat", "patty": "Beef", "toppings": ["Lettuce", 123]}
#     with pytest.raises(marshmallow.ValidationError) as e:
#         BurgerSchema().load(data)
#     if not "toppings" in e.value.messages:
#         pytest.fail()
#     assert "toppings" in e.value.messages


# def test_empty_toppings():
#     data = {"bread": "Whole wheat", "patty": "Beef", "toppings": []}
#     try:
#         validated_data = BurgerSchema().load(data)
#     except Exception as e:
#         pytest.fail(f"Schema validation failed with error: {e}")
#     assert validated_data == data


# def test_bread_false():
#     data = {"bread": False, "patty": "Beef", "sauce": "BBQ"}
#     with pytest.raises(marshmallow.ValidationError) as e:
#         BurgerSchema().load(data)
#     if not "bread" in e.value.messages:
#         pytest.fail()
#     assert "bread" in e.value.messages


# def test_patty_false():
#     data = {"bread": "Whole wheat", "patty": False, "sauce": "BBQ"}
#     with pytest.raises(marshmallow.ValidationError) as e:
#         BurgerSchema().load(data)
#     if not "patty" in e.value.messages:
#         pytest.fail()
#     assert "patty" in e.value.messages


# def test_sauce_false():
#     data = {"bread": "Whole wheat", "patty": "Beef", "sauce": False}
#     with pytest.raises(marshmallow.ValidationError) as e:
#         BurgerSchema().load(data)
#     if not "sauce" in e.value.messages:
#         pytest.fail()
#     assert "sauce" in e.value.messages


# def test_toppings_false():
#     data = {"bread": "Whole wheat", "patty": "Beef", "toppings": False}
#     with pytest.raises(marshmallow.ValidationError) as e:
#         BurgerSchema().load(data)
#     if not "toppings" in e.value.messages:
#         pytest.fail()
#     assert "toppings" in e.value.messages


# def test_toppings_contain_false():
#     data = {"bread": "Whole wheat", "patty": "Beef", "toppings": ["Lettuce", False]}
#     try:
#         BurgerSchema().load(data)
#         assert False
#     except marshmallow.ValidationError as e:
#         assert "toppings" in e.messages
