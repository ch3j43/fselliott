from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from fselliott import settings
from fselliott.models import Vendor, Customer
from django.template.context import RequestContext
from fselliott.forms import VendorForm

@login_required
def home(request):
    info = {}
    return render_to_response('interface/home.html', info)

@login_required
def vendors(request):
    info = {}
    vendor_list = Vendor.objects.all()
    info['vendors'] =  vendor_list
    return render_to_response('interface/vendors.html', info)

@login_required
def add_vendor(request):
    info = {}
    context_instance = RequestContext(request)
    form = VendorForm()
    info['form'] =  form
    return render_to_response('interface/vendor_add.html', info, context_instance)

@login_required
def customers(request):
    info = {}
    customers = Customer.objects.all()
    info['costumers'] =  customers
    return render_to_response('interface/customers.html', info)