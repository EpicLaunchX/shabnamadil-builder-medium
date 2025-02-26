from marshmallow import fields, Schema, validates, ValidationError


class BurgerSchema(Schema):
    bread = fields.String(required=True)
    patty = fields.String(required=True)

    @validates("bread")
    def validate_bread(self, value):
        if not isinstance(value, str):
            raise ValidationError("This field must be a string")

        if value is None or value == "":
            raise ValidationError("This field is required")

    @validates("patty")
    def validate_patty(self, value):
        if not isinstance(value, str):
            raise ValidationError("This field must be a string")
        if value is None or value == "":
            raise ValidationError("This field is required")
