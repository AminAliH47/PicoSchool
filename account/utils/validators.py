from re import match

from django.core.exceptions import ValidationError


def validate_phone_number(value):
    if not bool(match(pattern=r"^09\d{9}$", string=value)):
        raise ValidationError(message="شماره تلفن معتبر نمیباشد.")

