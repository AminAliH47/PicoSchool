import re

from django.core.exceptions import ValidationError


def is_valid_national_code(input):
    if not re.search(r'^\d{10}$', input):
        raise ValidationError('لطفا کدملی معتبر وارد کنید')
    # elif input == str:
        # raise ValidationError('لطفا کدملی معتبر وارد کنید')
    else:
        check = int(input[9])
        s = sum([int(input[x]) * (10 - x) for x in range(9)]) % 11
        return (s < 2 and check == s) or (s >= 2 and check + s == 11)
