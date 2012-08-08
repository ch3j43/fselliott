from django.core.exceptions import ValidationError

def validate_spaces(value):
    stripped = ""
    try:
        stripped = str(value).strip()
    except Exception as e:
        raise ValidationError('This field is required.')
    if stripped == "":
        raise ValidationError('This field is required.')