from django.shortcuts import render_to_response, redirect
from django.contrib.auth.decorators import login_required
from fselliott import settings
from fselliott.models import Vendor, Customer, Contact
from django.template.context import RequestContext
from fselliott.forms import VendorForm
from fselliott.helper import save_vendor
from django.contrib import messages

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
    
    if request.method == "POST":
        print request.POST
        form = VendorForm(request.POST)
        res = save_vendor(request.POST)
        if res:
            messages.success(request,'New vendor added.')
        else:
            messages.warning(request,'Error adding new vendor.')
        return redirect('add_vendor')
    
    info['form'] =  form
    info['heading'] = 'Add Vendor'
    return render_to_response('interface/vendor_add.html', info, context_instance)

@login_required
def edit_vendor(request, vid=None):
    
    if not vid:
        return redirect('vendors')
    
    info = {}
    context_instance = RequestContext(request)
    
    vendor = Vendor.objects.get(id=vid)
    form = VendorForm(initial={
        'company':vendor.company,
        'nature_of_business':vendor.business_nature.id,
        'address1':vendor.address1,
        'address2':vendor.address2,
        'city_municipality':vendor.city_municipality,
        'state_region_province':vendor.state_region_province,
        'country':vendor.country.id,
        'telephone':vendor.telephone,
        'fax':vendor.fax,
        'date_accredited':vendor.date_accredited})
    
    if request.method == "POST":
        form = VendorForm(request.POST)
        if form.is_valid():
            data = {}
            data = form.cleaned_data
            data['id'] = vid
            res = save_vendor(data)
            if res:
                messages.success(request,'Edit vendor success.')
            else:
                messages.warning(request,'Error editing vendor.')
            return redirect('add_vendor')
    
    info['form'] =  form
    info['heading'] = 'Edit Vendor'
    return render_to_response('interface/vendor_add.html', info, context_instance)

@login_required
def vendor_contact_details(request, vid=None):
    
    if not vid:
        return redirect('vendors')    
    info = {}
    
    vendor = Vendor.objects.get(id=vid)
    contacts = Contact.objects.filter(vendor__id=vendor.id)
    vendors = Vendor.objects.all()
    
    info['contacts'] = contacts
    info['vendor'] = vendor
    info['vendors'] = vendors
    return render_to_response('interface/contact_details.html', info)

@login_required
def new_vendor_contact(request, frm=None, vid=None):
    if not vid:
        return redirect('vendors')
    
    if not frm:
        return redirect('vendors')
     
    info = {}
    context_instance = RequestContext(request)
    vendor = Vendor.objects.get(id=vid)
    
    info['vendor'] = vendor
    return render_to_response('interface/add_contact_details.html', info, context_instance)

@login_required
def customers(request):
    info = {}
    customers = Customer.objects.all()
    info['costumers'] =  customers
    return render_to_response('interface/customers.html', info)