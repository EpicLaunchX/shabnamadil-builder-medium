import pytest
from marshmallow import ValidationError

from pytemplate.domain.models import Burger
from pytemplate.service.burger import BurgerBuilder, CheeseBurgerBuilder, ChickenBurgerBuilder


def test_abstract_class_cannot_be_instantiated():
    with pytest.raises(TypeError):
        BurgerBuilder()
    pass


def test_not_implemented_error():

    class TestBurgerBuilder(BurgerBuilder):
        def bread(self, bread):
            return super().bread(bread)

        def meat(self, meat: str):
            return super().meat(meat)

        def patty(self, patty):
            return super().patty(patty)

        def sauce(self, sauce: str):
            return super().sauce(sauce)

        def toppings(self, toppings: list[str]):
            return super().toppings(toppings)

        def build(self):
            return super().build()

    builder = TestBurgerBuilder()

    with pytest.raises(NotImplementedError):
        builder.bread("Whole wheat")

    with pytest.raises(NotImplementedError):
        builder.patty("Chicken")

    with pytest.raises(NotImplementedError):
        builder.sauce("Mayo")

    toppings_list = ["Lettuce", "Tomato"]
    with pytest.raises(NotImplementedError):
        builder.toppings(toppings_list)

    with pytest.raises(NotImplementedError):
        builder.build()


def test_cheeseburger_builder_full():
    toppings_list = ["Lettuce", "Tomato"]
    data = {"bread": "Whole wheat", "patty": "Cheese", "sauce": "Mayo", "toppings": toppings_list}
    builder = CheeseBurgerBuilder().bread("Whole wheat").patty("Cheese").sauce("Mayo").toppings(toppings_list)
    cheese_burger = builder.build()

    assert cheese_burger.bread == data["bread"]
    assert cheese_burger.patty == data["patty"]
    assert cheese_burger.sauce == data["sauce"]
    assert cheese_burger.toppings == data["toppings"]
    assert cheese_burger.__str__() == "Burger with Whole wheat bread, Cheese patty. Sauce: Mayo, Toppings: Lettuce, Tomato"
    assert isinstance(cheese_burger, Burger)
    assert isinstance(builder, CheeseBurgerBuilder)


def test_cheeseburger_builder_minimal():
    builder = CheeseBurgerBuilder().bread("Sesame").patty("Chicken")
    burger = builder.build()

    assert burger.bread == "Sesame"
    assert burger.patty == "Chicken"
    assert burger.sauce is None
    assert burger.toppings is None


def test_cheeseburger_builder_no_toppings():
    builder = CheeseBurgerBuilder().bread("Brioche").patty("Turkey").sauce("Mayo").toppings([])
    burger = builder.build()

    assert burger.bread == "Brioche"
    assert burger.patty == "Turkey"
    assert burger.sauce == "Mayo"
    assert burger.toppings == []


def test_cheeseburger_builder_invalid_bread():
    builder = CheeseBurgerBuilder()

    with pytest.raises(ValidationError):
        builder.bread(123).patty("Beef").build()


def test_cheeseburger_builder_invalid_patty():
    builder = CheeseBurgerBuilder()

    with pytest.raises(ValidationError):
        builder.bread("White").patty(789).build()


def test_cheeseburger_builder_invalid_sauce():
    builder = CheeseBurgerBuilder()

    with pytest.raises(ValidationError):
        builder.bread("White").patty("Beef").sauce(99).build()


def test_cheeseburger_builder_invalid_toppings():
    builder = CheeseBurgerBuilder()

    with pytest.raises(ValidationError):
        builder.bread("White").patty("Beef").toppings("Not a list").build()


def test_cheeseburger_builder_toppings_with_invalid_items():
    builder = CheeseBurgerBuilder()

    with pytest.raises(ValidationError):
        builder.bread("White").patty("Beef").toppings(["Lettuce", 123]).build()


def test_chickenburger_builder_full():
    toppings_list = ["Lettuce", "Tomato"]
    data = {"bread": "Whole wheat", "patty": "Chicken", "sauce": "BBQ", "toppings": toppings_list}
    builder = ChickenBurgerBuilder().bread("Whole wheat").patty("Chicken").sauce("BBQ").toppings(toppings_list)
    chicken_burger = builder.build()

    assert chicken_burger.bread == data["bread"]
    assert chicken_burger.patty == data["patty"]
    assert chicken_burger.sauce == data["sauce"]
    assert chicken_burger.toppings == data["toppings"]
    assert chicken_burger.__str__() == "Burger with Whole wheat bread, Chicken patty. Sauce: BBQ, Toppings: Lettuce, Tomato"
    assert isinstance(chicken_burger, Burger)
    assert isinstance(builder, ChickenBurgerBuilder)


def test_chickenburger_builder_minimal():
    builder = ChickenBurgerBuilder().bread("Sesame").patty("Chicken")
    burger = builder.build()

    assert burger.bread == "Sesame"
    assert burger.patty == "Chicken"
    assert burger.sauce is None
    assert burger.toppings is None


def test_chickenburger_builder_no_toppings():
    builder = ChickenBurgerBuilder().bread("Brioche").patty("Turkey").sauce("Mayo").toppings([])
    burger = builder.build()

    assert burger.bread == "Brioche"
    assert burger.patty == "Turkey"
    assert burger.sauce == "Mayo"
    assert burger.toppings == []


def test_chicken_burger_builder_invalid_bread():
    builder = ChickenBurgerBuilder()

    with pytest.raises(ValidationError):
        builder.bread(123).patty("Beef").build()


def test_chickenburger_builder_invalid_patty():
    builder = ChickenBurgerBuilder()

    with pytest.raises(ValidationError):
        builder.bread("White").patty(789).build()


def test_chickenburger_builder_invalid_sauce():
    builder = ChickenBurgerBuilder()

    with pytest.raises(ValidationError):
        builder.bread("White").patty("Beef").sauce(99).build()


def test_chickenburger_builder_invalid_toppings():
    builder = ChickenBurgerBuilder()

    with pytest.raises(ValidationError):
        builder.bread("White").patty("Beef").toppings("Not a list").build()


def test_chickenburger_builder_toppings_with_invalid_items():
    builder = ChickenBurgerBuilder()

    with pytest.raises(ValidationError):
        builder.bread("White").patty("Beef").toppings(["Lettuce", 123]).build()
