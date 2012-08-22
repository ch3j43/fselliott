from fselliott.models import Vendor, Contact, Customer
from common.models import Country, NatureOfBusiness, Department

def save_vendor(data):
    try:
        try:
            vendor = Vendor.objects.get(id=data['id'])
        except:
            vendor = Vendor()
        
        vendor.company = data['company']
        vendor.address1 = data['address1']
        vendor.address2 = data['address2']
        vendor.city_municipality = data['city_municipality']
        vendor.state_region_province = data['state_region_province']
        
        country = Country.objects.get(id=data['country'])    
        vendor.country = country
        vendor.telephone = data['telephone']
        vendor.fax = data['fax']
        
        nature_of_business = NatureOfBusiness.objects.get(id=data['nature_of_business'])
        vendor.business_nature = nature_of_business
        vendor.date_accredited = data['date_accredited']
        vendor.save()
        return True
    except:
        return False
    
def save_contact(data):
    try:
        try:
            contact = Contact.objects.get(id=data['id'])
        except:
            contact = Contact()
            
        contact.name = data['name']
        contact.position = data['position']
        contact.email = data['email']
        contact.mobile = data['mobile']
        contact.telephone = data['telephone']
        contact.fax = data['fax']
        contact.department = Department.objects.get(id=data['department'])
        
        try:
            if data['vid']:
                contact.vendor = Vendor.objects.get(id=data['vid'])
            elif data['cid']:
                contact.customer = Customer.objects.get(id=data['cid'])
            else:
                return False
        except:
            return False
        
        contact.save()
        return True
    except:
        return False
    
def save_customer(data):
    try:
        try:
            customer = Customer.objects.get(id=data['id'])
        except:
            customer = Customer()
        
        customer.company_name = data['company_name']
        customer.telephone = data['telephone']
        customer.fax = data['fax']
        customer.business_nature = NatureOfBusiness.objects.get(id=data['nature_of_business'])
        customer.save()
        return True
    except:
        return False
        
        