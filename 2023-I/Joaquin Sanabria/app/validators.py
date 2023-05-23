from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

class UppercaseValidator:
    def __init__(self, min_uppercase=2):
        self.min_uppercase = min_uppercase

    def validate(self, password, user=None):
        if sum(c.isupper() for c in password) < self.min_uppercase:
            raise ValidationError(_("This password must contain at least %(min_uppercase)d uppercase letters."),
                code='password_no_uppercase',
                params={'min_uppercase': self.min_uppercase},)

    def get_help_text(self):
        return _("Your password must contain at least %(min_uppercase)d uppercase letters."% {'min_uppercase': self.min_uppercase})
