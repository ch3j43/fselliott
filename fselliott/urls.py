from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from fselliott import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'inventory.views.home', name='home'),
    # url(r'^inventory/', include('inventory.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', "django.views.static.serve", {'document_root': settings.MEDIA_ROOT}),
)

urlpatterns += patterns('fselliott.views.interface',
    url(r'^$', 'home', {}, name='home'),
    url(r'^vendors/$', 'vendors', {}, name='vendors'),
    url(r'^vendors/add$', 'add_vendor', {}, name='add_vendor'),
    url(r'^vendors/edit/(?P<vid>\w+)', 'edit_vendor', {}, name='edit_vendor'),
    url(r'^vendor/contacts/(?P<vid>\w+)', 'vendor_contact_details', {}, name="vendor_contacts"),
    url(r'^vendor/new_contacts/(?P<vid>\w+)', 'new_vendor_contact', {}, name="new_vendor_contact"),
    url(r'^vendor/edit_contact/(?P<cid>\w+)', 'edit_vendor_contact', {}, name="edit_vendor_contact"),
    url(r'^contact/delete$', 'delete_contact', {}, name='delete_contact'),
    url(r'^customers/$', 'customers', {}, name='customers'),
    url(r'^customers/add$', 'new_customer', {}, name='new_customer'),
)

urlpatterns += patterns('fselliott.views.auth',
    url(r'^login/*$','auth_login', {}, name='login'),
    url(r'^logout/$','auth_logout', {}, name='logout'),
)
