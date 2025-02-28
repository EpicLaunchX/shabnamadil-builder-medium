import pytest

from typing import List
from pytemplate.service.burger import BurgerBuilder


class TestBurgerBuilder(BurgerBuilder):
    def bread(self, bread):
        super().bread(bread)

    def meat(self, meat: str):
        super().meat(meat)

    def patty(self, patty):
        super().patty(patty)

    def sauce(self, sauce: str):
        super().sauce(sauce)

    def toppings(self, toppings: List[str]):
        super().toppings(toppings)
    
    def build(self):
        super().build()


def test_not_implemented_error():
    builder = TestBurgerBuilder()

    with pytest.raises(NotImplementedError):
        builder.bread("Whole wheat")

    with pytest.raises(NotImplementedError):
        builder.meat("Beef")

    with pytest.raises(NotImplementedError):
        builder.patty("Chicken")

    with pytest.raises(NotImplementedError):
        builder.sauce("Mayo")

    toppings_list = ["Lettuce", "Tomato"]
    with pytest.raises(NotImplementedError):
        builder.toppings(toppings_list)

    with pytest.raises(NotImplementedError):
        builder.build()


def test_abstract_class_cannot_be_instantiated():
    with pytest.raises(TypeError):
        BurgerBuilder()
    pass
