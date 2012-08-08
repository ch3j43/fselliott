from django.contrib import admin
from common.models import NatureOfBusiness, Department, Country

class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')

admin.site.register(NatureOfBusiness)
admin.site.register(Department)
admin.site.register(Country, CountryAdmin)
