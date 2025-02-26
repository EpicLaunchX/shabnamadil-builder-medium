import marshmallow


class BurgerSchema(marshmallow.Schema):
    bread = marshmallow.fields.String(required=True)
    patty = marshmallow.fields.String(required=True)

    @marshmallow.validates("bread")
    def validate_bread(self, value):
        if value is None or value == "":
            raise marshmallow.ValidationError("Bread field is required")

    @marshmallow.validates("patty")
    def validate_patty(self, value):
        if value is None or value == "":
            raise marshmallow.ValidationError("Patty field is required")


def burger_factory(data):
    try:
        validated_data = BurgerSchema().load(data)
        return validated_data
    except marshmallow.ValidationError as err:
        return {"errors": err.messages}
