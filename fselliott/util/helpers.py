from django.forms.fields import CharField
from fselliott.util.validators import validate_spaces
from django.utils.translation import ugettext_lazy as _

def add_selector_to_choices(selector_text="Please Select One",choices=None,index=''):
    clean_choices = []
    clean_choices.append((index,selector_text))
    for id,name in choices:
        clean_choices.append((id,name))
    return clean_choices

class CustomCharField(CharField):
    default_error_messages = {
        'invalid': _(u'Enter a valid e-mail address.'),
    }
    default_validators = [validate_spaces]

    def clean(self, value):
        value = self.to_python(value).strip()
        return super(CustomCharField, self).clean(value)
