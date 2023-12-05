from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from import_export.fields import Field
from .models import *

#admin.site.register(Vehicle)
admin.site.register(User)
#admin.site.register(Article)
# admin.site.register(BuildingSite)
admin.site.register(Delivery_note)
admin.site.register(Combination)
#admin.site.register(Customer)
#admin.site.register(Supplier)
# admin.site.register(Forwarders)
# admin.site.register(Transaction)
admin.site.register(Yard_list)
admin.site.register(Settings)
admin.site.register(Contract)

class ArticleResource(resources.ModelResource):
    # id = Field(attribute = 'id', column_name= 'ARTIKEL')
    name = Field(attribute = 'name', column_name='BEZEICH1')
    description = Field(attribute='description', column_name='BEZEICH2')
    short_name = Field(attribute='short_name', column_name='MC')
    entry_weight = Field(attribute='entry_weight', column_name='INPUT')
    outgoing_weight = Field(attribute='outgoing_weight', column_name='OUTPUT') 
    price1 = Field(attribute='price1', column_name='KOST')
    group = Field(attribute='group', column_name='GRUPPE')
    # minimum_amount = Field(attribute="minimum_amount", column_name='MINMENGE')

    class Meta:
        model = Article

class CustomerResource(resources.ModelResource):
    name = Field(attribute = 'name', column_name='NAME1')
    firstname = Field(attribute = 'firstname', column_name='NAME2')
    salutation = Field(attribute = 'salutation', column_name='ANDREDE')
    street = Field(attribute = 'street', column_name='STRASSE')
    pin = Field(attribute = 'pin', column_name='PLZ')
    place = Field(attribute = 'place', column_name='ORT')
    website = Field(attribute = 'website', column_name='INTERNET')
    country = Field(attribute = 'country', column_name='LAND')
    contact_person1_email = Field(attribute = 'contact_person1_email', column_name='EMAIL')

    class Meta:
        model = Customer

class VehicleResource(resources.ModelResource):
    license_plate = Field(attribute='license_plate', column_name='KENNZEICH')
    country = Field(attribute='country', column_name='LAND')
    telephone = Field(attribute='telephone', column_name='TELEFON')
    vehicle_weight = Field(attribute='vehicle_weight', column_name='TARA')
    # vehicle_weight2 = Field(attribute='vehicle_weight2',column_name='TARA2')
    created_date_time = Field(attribute='created_date_time', column_name='DATUM')
    vehicle_type = Field(attribute='vehicle_type', column_name='TYP')

    class Meta:
        model = Vehicle

class BuildingSiteResource(resources.ModelResource):
    name = Field(attribute='name', column_name='NAME1')
    short_name = Field(attribute='short_name', column_name='MC')
    place = Field(attribute='place', column_name='ORT')
    street = Field(attribute='street', column_name='STRASSE')
    pin = Field(attribute='pin', column_name='PLZ')

    class Meta:
        model = BuildingSite

class SupplierResource(resources.ModelResource):
    supplier_name = Field(attribute='supplier_name', column_name='NAME1')
    street = Field(attribute='street', column_name='STRASSE')
    pin = Field(attribute='pin', column_name='PLZ')
    fax = Field(attribute='fax', column_name='TELEFAX')
    place = Field(attribute='place', column_name='ORT')

    class Meta:
        model = Supplier


@admin.register(BuildingSite)
class BuildingSiteAdmin(ImportExportModelAdmin):
    resource_class = BuildingSiteResource

@admin.register(Customer)
class CustomerAdmin(ImportExportModelAdmin):
    resource_class = CustomerResource

@admin.register(Forwarders)
class ForwardersAdmin(ImportExportModelAdmin):
    pass

@admin.register(Supplier)
class SupplierAdmin(ImportExportModelAdmin):
    resource_class = SupplierResource

@admin.register(Transaction)
class TransactionAdmin(ImportExportModelAdmin):
    pass

@admin.register(Article)
class ArticleAdmin(ImportExportModelAdmin):
    resource_class = ArticleResource

@admin.register(Vehicle)
class VehicleAdmin(ImportExportModelAdmin):
    resource_class = VehicleResource