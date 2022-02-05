import re

from django.core.exceptions import ValidationError
from django.core.validators import URLValidator, EmailValidator


def validate_contact_link(contact_link: str) -> None:
    try:
        URLValidator()(contact_link)
    except ValidationError:
        email = re.search(r'mailto:(.*)', contact_link)
        if not email:
            raise ValidationError('The value is neither a link nor a "mailto:<email>"')
        EmailValidator()(email.group(1))
