from pytemplate.service.burger import ChickenBurgerBuilder, CheeseBurgerBuilder, VeggieBurgerBuilder
from marshmallow import ValidationError


def get_choice_input():
    try:
        return str(input("Please choose choice. Valid choices: chicken, vegan, cheese"))
    except:
        raise ValidationError("Invalid choice!")
    

def main():
    choice = get_choice_input().lower()
    try:
        if choice == 'chicken':
            return ChickenBurgerBuilder().bread("Sesame Seed Bun").patty("Chicken").sauce("Ketchup").toppings(["Lettuce", "Tomato"]).build()
        if choice == 'cheese':
            return CheeseBurgerBuilder().bread("Sesame Seed Bun").patty("Beef").sauce("Ketchup").toppings(["Lettuce", "Tomato"]).build()
        if choice == 'veggie':
            return VeggieBurgerBuilder().bread("Sesame Seed Bun").patty("Veggie").sauce("Ketchup").toppings(["Lettuce", "Tomato"]).build()
        
    except ValidationError as err:
        raise ValidationError("Invalid choice!") from err