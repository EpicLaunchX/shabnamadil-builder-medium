import pytest

from pytemplate.domain.models import Burger


def test_valid_burger():
    burger = Burger(bread="Whole Wheat", patty="Chicken", sauce="BBQ", toppings=["Lettuce", "Tomato"])
    expected_burger = Burger(bread="Whole Wheat", patty="Chicken", sauce="BBQ", toppings=["Lettuce", "Tomato"])
    assert burger == expected_burger


def test_required_bread():
    with pytest.raises(TypeError):
        Burger(patty="Chicken", sauce="BBQ", toppings=["Lettuce", "Tomato"])


def test_required_patty():
    with pytest.raises(TypeError):
        Burger(bread="Whole Wheat", sauce="BBQ", toppings=["Lettuce", "Tomato"])


def test_optional_values():
    burger = Burger(bread="Whole Wheat", patty="Chicken")
    assert burger.sauce == None
    assert burger.toppings == None


def test_bread_value_type():
    with pytest.raises(ValueError):
        Burger(bread=5, patty="Chicken", sauce="BBQ", toppings=["Lettuce", "Tomato"])


def test_patty_value_type():
    with pytest.raises(ValueError):
        Burger(bread="Whole wheat", patty=5, sauce="BBQ", toppings=["Lettuce", "Tomato"])


def test_sauce_value_type():
    with pytest.raises(ValueError):
        Burger(bread="Whole wheat", patty="Chicken", sauce=5, toppings=["Lettuce", "Tomato"])


def test_toppings_value_type():
    with pytest.raises(ValueError):
        Burger(bread="Whole wheat", patty="Chicken", sauce="BBQ", toppings=5)


def test_toppings_item_type():
    with pytest.raises(ValueError):
        Burger(bread="Whole wheat", patty="Chicken", sauce="BBQ", toppings=[6, "Tomato"])


def test_toppings_empty_list():
    burger = Burger(bread="Whole wheat", patty="Chicken", sauce="BBQ", toppings=[])
    assert burger.toppings == []


def test_str_method():
    burger = Burger(bread="Whole wheat", patty="Chicken", sauce="BBQ", toppings=["Lettuce", "Tomato"])
    assert str(burger) == "Burger with Whole wheat bread, Chicken patty. Sauce: BBQ, Toppings: Lettuce, Tomato"


def test_default_str_method():
    burger = Burger(bread="Whole wheat", patty="Chicken")
    assert str(burger) == "Burger with Whole wheat bread, Chicken patty. Sauce: No sauce, Toppings: No toppings"
