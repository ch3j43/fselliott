from fselliott.models import Vendor
from common.models import Country, NatureOfBusiness

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