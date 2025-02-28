from abc import ABC, abstractmethod


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
