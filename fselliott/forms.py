from django import forms
from fselliott.util.helpers import add_selector_to_choices, CustomCharField
from django.forms.widgets import PasswordInput
from django.utils.translation import ugettext_lazy as _
from common.models import Country

class LogInForm(forms.Form):
    username = CustomCharField(label=_("Username"), max_length=24, required=True, widget=forms.TextInput(attrs={'class':'span12'}))
    password = CustomCharField(label=_("Password"), max_length=32, required=True, widget=PasswordInput(attrs={'class':'span12'}))
    
class VendorForm(forms.Form):
    company = CustomCharField(label=_("Company Name"), required=True, widget=forms.TextInput(attrs={'class':'span6'}))
    address1 = CustomCharField(label=_("Address1"), required=True, widget=forms.Textarea(attrs={'class':'span6'}))
    address2 = CustomCharField(label=_("Address2"), required=False, widget=forms.Textarea(attrs={'class':'span6'}))
    city_municipality = CustomCharField(label=_("City/Municipality"), required=True, widget=forms.TextInput(attrs={'class':'span6'}))
    state_region_province = CustomCharField(label=_("State/Region/Province"), required=True, widget=forms.TextInput(attrs={'class':'span6'}))
    
    countries = Country.objects.all().values_list('id','name')
    country = forms.ChoiceField(label=_("Country"), choices=countries, widget=forms.Select(attrs={'class':'span6'}))
