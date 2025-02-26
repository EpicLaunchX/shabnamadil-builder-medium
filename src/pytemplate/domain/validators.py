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


def burger_factory(data):
    try:
        validated_data = BurgerSchema().load(data)
        return validated_data
    except marshmallow.ValidationError as err:
        return {"errors": err.messages}
