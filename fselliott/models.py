from django.db import models
from common.models import Department, NatureOfBusiness, Country
		
class Customer(models.Model):
	id = models.AutoField(db_column='id', primary_key=True)
	company_name = models.CharField(db_column='company_name', max_length=255)
	telephone = models.CharField(db_column='telephone', max_length=100)
	fax = models.CharField(db_column='fax', max_length=100)
	business_nature = models.ForeignKey(NatureOfBusiness, db_column='nature_of_business_id', null=True)
	created = models.DateField(db_column='created_date', auto_now_add=True, blank=True)
	
	class Meta:
		db_table = 'customers'
		ordering = ['id']
		verbose_name = 'Customers'

class Vendor(models.Model):
	id = models.AutoField(db_column='id', primary_key=True)
	company = models.CharField(db_column='company', max_length=255)
	address1 = models.CharField(db_column='address1', max_length=255)
	address2 = models.CharField(db_column='address2', max_length=255)
	city_municipality = models.CharField(db_column='city_municipality', max_length=255)
	state_region_province = models.CharField(db_column='state_region_province', max_length=255)
	country = models.ForeignKey(Country, db_column='country_id', null=True)
	telephone = models.CharField(db_column='telephone', max_length=100,blank=True)
	fax = models.CharField(db_column='fax', max_length=100,blank=True)
	nature_of_business = models.CharField(db_column='nature_of_business', max_length=255, blank=True)
	date_accredited = models.CharField(db_column='date_accredited', max_length=100)
	business_nature = models.ForeignKey(NatureOfBusiness, db_column='nature_of_business_id', null=True)
	created = models.DateField(db_column='created_date', auto_now_add=True, blank=True)

	class Meta:
		db_table = 'vendors'
		ordering = ["id"]
		verbose_name = 'Vendor'

class Accreditation(models.Model):
	id = models.AutoField(db_column='id', primary_key=True)
	vendor = models.ForeignKey(Vendor, db_column='vendor_id')
	scan_docs = models.CharField(db_column='scan_docs',max_length=100)
	uploaded_by = models.IntegerField(db_column='uploaded_by')
	created = models.DateField(db_column='created_date', auto_now_add=True, blank=True)

	class Meta:
		db_table = 'accreditations'
		ordering = ["id"]
		verbose_name = 'Accreditations'

class Contact(models.Model):
	id = models.AutoField(db_column='id', primary_key=True)
	name = models.CharField(db_column='name', max_length=255)
	position = models.CharField(db_column='position', max_length=255)
	department = models.ForeignKey(Department, db_column='department_id')
	email = models.CharField('email', max_length=100)
	mobile = models.CharField('mobile', max_length=100)
	telephone = models.CharField('telephone', max_length=100)
	fax = models.CharField('fax', max_length=100)
	vendor = models.ForeignKey(Vendor, db_column='vendor_id', null=True)
	customer = models.ForeignKey(Customer, db_column='customer_id', null=True)
	created = models.DateField(db_column='created_date', auto_now_add=True, blank=True)
	
	class Meta:
		db_table = 'contacts'
		ordering = ['name']
		verbose_name = 'Contacts'
		
class Item(models.Model):
	id = models.AutoField(db_column='id', primary_key=True)
	name = models.CharField(db_column='name', max_length=255)
	note = models.CharField(db_column='note', max_length=255)
	created = models.DateField(db_column='created_date', auto_now_add=True, blank=True)
	
	class Meta:
		db_table = 'items'
		ordering = ['created']
		verbose_name = 'Items'
		
class ItemSpecification(models.Model):
	id = models.AutoField(db_column='id', primary_key=True)
	specification = models.CharField(db_column='specification', max_length=255)
	item = models.ForeignKey(Item, db_column='item_id')
	
	class Meta:
		db_table = 'item_specifications'
		ordering = ['id']
		verbose_name = 'Item Specifications'
		
class ItemNote(models.Model):
	id = models.AutoField(db_column='id', primary_key=True)
	note = models.CharField(db_column='note', max_length=255)
	item = models.ForeignKey(Item, db_column='item_id')
	created = models.DateField(db_column='created_date', auto_now_add=True, blank=True)
	
	class Meta:
		db_table = 'item_notes'
		ordering = ['id']
		verbose_name = 'Item Notes'
	
	
