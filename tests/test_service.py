import pytest

from pytemplate.service.burger import BurgerBuilder

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
