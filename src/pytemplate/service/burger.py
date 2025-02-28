from abc import ABC, abstractmethod

from pytemplate.domain.models import burger_factory


class BurgerBuilder(ABC):

    @abstractmethod
    def bread(self, bread: str):
        raise NotImplementedError("bread() must be implemented by subclasses")

    @abstractmethod
    def meat(self, meat: str):
        raise NotImplementedError("meat() must be implemented by subclasses")

    @abstractmethod
    def patty(self, patty: str):
        raise NotImplementedError("patty() must be implemented by subclasses")

    @abstractmethod
    def sauce(self, sauce: str):
        raise NotImplementedError("sauce() must be implemented by subclasses")

    @abstractmethod
    def toppings(self, toppings: list[str]):
        raise NotImplementedError("toppings() must be implemented by subclasses")

    @abstractmethod
    def build(self):
        raise NotImplementedError("build() must be implemented by subclasses")


class CheeseBurgerBuilder(BurgerBuilder):
    def __init__(self):
        pass

    def bread(self, bread):
        self._bread = bread
        return self

    def patty(self, patty):
        self._patty = patty
        return self

    def sauce(self, sauce):
        self._sauce = sauce
        return self

    def toppings(self, toppings):
        self._toppings = toppings
        return self

    def build(self):
        data = {"bread": self.bread(), "patty": self.patty(), "sauce": self.sauce(), "toppings": self.toppings()}
        return burger_factory(data)
