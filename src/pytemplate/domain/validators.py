from marshmallow import fields, Schema, validates, ValidationError


class BurgerSchema(Schema):
    bread = fields.String(required=True)
    patty = fields.String(required=True)

    @validates("bread")
    def validate_bread(self, value):
        if not isinstance(value, str):
            raise ValidationError("Bread field must be a string")

        if value is None or value == "":
            raise ValidationError("Bread field is required")

    @validates("patty")
    def validate_patty(self, value):
        if not isinstance(value, str):
            raise ValidationError("Bread field must be a string")
        if value is None or value == "":
            raise ValidationError("Bread field is required")


def burger_factory(data):
    try:
        validated_data = BurgerSchema().load(data)
        return validated_data
    except ValidationError as err:
        return {"errors": err.messages}
