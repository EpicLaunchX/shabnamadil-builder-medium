import pytest

from pytemplate.service.burger import BurgerBuilder


class TestBurgerBuilder(BurgerBuilder):
    def bread(self, bread: str):
        raise NotImplementedError("bread() is not implemented in TestBurgerBuilder")

    def meat(self, meat: str):
        raise NotImplementedError("meat() is not implemented in TestBurgerBuilder")

    def patty(self, patty: str):
        raise NotImplementedError("patty() is not implemented in TestBurgerBuilder")

    def sauce(self, sauce: str):
        raise NotImplementedError("sauce() is not implemented in TestBurgerBuilder")

    def toppings(self, toppings: list[str]):
        raise NotImplementedError("toppings() is not implemented in TestBurgerBuilder")

    def build(self):
        raise NotImplementedError("build() is not implemented in TestBurgerBuilder")


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
