from marshmallow import fields, Schema, ValidationError


def validate_field_type(value):
    if not isinstance(value, str):
        raise ValidationError("This field must be a string")


def validate_required(value):
    if value is None or value == "":
        raise ValidationError("This field is required")


class BurgerSchema(Schema):
    bread = fields.String(required=True, validate=[validate_field_type, validate_required])
    patty = fields.String(required=True, validate=[validate_field_type, validate_required])


def burger_factory(data):
    try:
        validated_data = BurgerSchema().load(data)
        return validated_data
    except ValidationError as err:
        return {"errors": err.messages}
