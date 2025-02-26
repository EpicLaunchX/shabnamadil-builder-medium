import marshmallow


class BurgerSchema(marshmallow.Schema):
    bread = marshmallow.fields.String(required=True)
    patty = marshmallow.fields.String(required=True)
    sauce = marshmallow.fields.String(allow_none=True)
    toppings = marshmallow.fields.List(marshmallow.fields.String(), allow_none=True)

    @marshmallow.validates("bread")
    def validate_bread(self, value):
        if not isinstance(value, str) or not value.strip():
            raise marshmallow.ValidationError("Bread field must be a non-empty string.")

    @marshmallow.validates("patty")
    def validate_patty(self, value):
        if not isinstance(value, str) or not value.strip():
            raise marshmallow.ValidationError("Patty field must be a non-empty string.")

    @marshmallow.validates("sauce")
    def validate_sauce(self, value):
        if value is not None and not isinstance(value, str):
            raise marshmallow.ValidationError("Sauce must be a string or None.")

    @marshmallow.validates("toppings")
    def validate_toppings(self, value):
        if value is not None:
            if not isinstance(value, list):
                raise marshmallow.ValidationError("Toppings must be a list.")
            if not all(isinstance(item, str) and item.strip() for item in value):
                raise marshmallow.ValidationError("All toppings must be non-empty strings.")


def burger_factory(data):
    try:
        validated_data = BurgerSchema().load(data)
        return validated_data
    except marshmallow.ValidationError as err:
        return {"errors": err.messages}
