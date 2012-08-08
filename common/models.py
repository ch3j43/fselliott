from django.db import models

class NatureOfBusiness(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    name = models.CharField(db_column='name', max_length=200, blank=True)
    
    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'nature_of_business'
        ordering = ["name"]
        verbose_name = 'Business Nature'

class Department(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    name = models.CharField(db_column='name', max_length=200, blank=True)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        db_table = 'departments'
        ordering = ["name"]
        verbose_name = 'Department'
        
class Country(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    name = models.CharField(db_column='name', max_length=100, blank=True)
    code = models.CharField(db_column='code', max_length=45, blank=True)
    
    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'countries'
        ordering = ["name"]
        verbose_name = 'Country'

