from dataclasses import dataclass
from typing import List, Optional

import marshmallow

from pytemplate.domain.validators import BurgerSchema


@dataclass
class Burger:
    bread: str
    patty: str
    sauce: Optional[str] = None
    toppings: Optional[List[str]] = None

    def __str__(self):
        toppings_str = ", ".join(self.toppings) if self.toppings else "no toppings"
        sauce_str = "no sauce" if self.sauce is None else self.sauce
        return f"Burger with {self.bread} bread, {self.patty} patty. Sauce: {sauce_str}, Toppings: {toppings_str}"

    def __post_init__(self):
        self._validate_bread_and_patty()
        self._validate_sauce()
        self._validate_toppings()

    def _validate_bread_and_patty(self):
        if not isinstance(self.bread, str) or not isinstance(self.patty, str):
            raise ValueError("Bread and patty must be strings")

    def _validate_sauce(self):
        if self.sauce and not isinstance(self.sauce, str):
            raise ValueError("Sauce value must be string")

    def _validate_toppings(self):
        if self.toppings:
            if not isinstance(self.toppings, list):
                raise ValueError("Toppings type must be list")
            if not all(isinstance(topping, str) for topping in self.toppings):
                raise ValueError("All toppings must be strings")


def burger_factory(data):
    try:
        validated_data = BurgerSchema().load(data)
        return Burger(**validated_data)
    except marshmallow.ValidationError as err:
        raise marshmallow.ValidationError(err.messages)
