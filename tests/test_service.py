import pytest

from pytemplate.service.burger import BurgerBuilder, CheeseBurgerBuilder


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

    # with pytest.raises(NotImplementedError):
    #     builder.meat("Beef")

    with pytest.raises(NotImplementedError):
        builder.patty("Chicken")

    with pytest.raises(NotImplementedError):
        builder.sauce("Mayo")

    toppings_list = ["Lettuce", "Tomato"]
    with pytest.raises(NotImplementedError):
        builder.toppings(toppings_list)

    with pytest.raises(NotImplementedError):
        builder.build()


def test_build_cheese_burger():
    toppings_list = ["Lettuce", "Tomato"]
    data = {"bread": "Whole wheat", "patty": "Chicken", "sauce": "BBQ", "toppings": toppings_list}
    cheese_burger = CheeseBurgerBuilder()
    cheese_burger.bread(data["bread"])
    cheese_burger.patty(data["patty"])
    cheese_burger.sauce(data["sauce"])
    cheese_burger.toppings(data["toppings"])
    cheese_burger.build()
    assert cheese_burger._bread == data["bread"]
    assert cheese_burger._patty == data["patty"]
    assert cheese_burger._sauce == data["sauce"]
    assert cheese_burger._toppings == data["toppings"]
