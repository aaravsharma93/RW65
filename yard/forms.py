from django import forms
from django.contrib.postgres.forms import SimpleArrayField

from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import password_validation
from django.contrib.auth import get_user_model

username_validator = UnicodeUsernameValidator()

yard_id_choices = (('1', 'Yard1'), ('2', 'Yard2'))
role_choices = (('technician', _('Technician')), ('superuser', _('Superuser')), ('operator', _('Operator')),
                ('selfservice', _('Self Service')))


class SignUpForm(UserCreationForm):
    name = forms.CharField(label=_('Name'), max_length=200, min_length=4, required=True, help_text='Required: Name',
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Name')}))
    email = forms.EmailField(label=_('E-mail'), max_length=50, help_text='Required: Inform a valid email address.',
                             widget=(forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('E-mail')})))
    password1 = forms.CharField(label=_('Password'),
                                widget=(
                                    forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': _('Password')})),
                                help_text='Required: valid password')

    # yard_id = forms.ChoiceField(label=_('Yard ID'),required=True,choices=yard_id_choices,widget=forms.Select(attrs={'class': 'form-control','placeholder': _('Yard ID')}))
    yard = forms.ModelChoiceField(label=_('Yard'), queryset=Yard_list.objects.all(), required=True,
                                  widget=forms.Select(attrs={'class': 'form-control'}))
    role = forms.ChoiceField(label=_('Role'), required=True, choices=role_choices,
                             widget=forms.Select(attrs={'class': 'form-control', 'placeholder': _('Role')}))

    class Meta:
        User = get_user_model()
        model = User
        fields = ('name', 'email', 'password1', 'yard', 'role')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # del self.fields['password1']
        del self.fields['password2']


class CustomLoginForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': _('Email')}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': _('Password'),
        }
    ))


class UserUpdateForm(forms.ModelForm):
    name = forms.CharField(label=_('Name'), max_length=200, min_length=4, required=True, help_text='Required: Name',
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Name')}))
    email = forms.EmailField(label=_('E-mail'), max_length=50, help_text='Required: Inform a valid email address.',
                             widget=(forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('E-mail')})))
    # yard_id = forms.ChoiceField(label=_('Yard ID'),required=True,choices=yard_id_choices,widget=forms.Select(attrs={'class': 'form-control','placeholder': _('Yard ID')}))
    yard = forms.ModelChoiceField(queryset=Yard_list.objects.all(), required=False,
                                  widget=forms.Select(attrs={'class': 'form-control'}))
    role = forms.ChoiceField(label=_('Role'), required=False, choices=role_choices,
                             widget=forms.Select(attrs={'class': 'form-control', 'placeholder': _('Role')}))

    class Meta:
        User = get_user_model()
        model = User
        fields = ('name', 'email', 'yard', 'role', 'address', 'telephone')
        labels = {
            'address': _('Address'),
            'telephone': _('Telephone')
        }


class CustomerForm(forms.ModelForm):
    delivery_terms = forms.ChoiceField(label=_('Delivery Terms'), widget=forms.Select(attrs={'class': 'form-control'}),
                                       choices=Customer.DELIVERY_CHOICES)
    price_group = forms.ChoiceField(label=_('Price Group'), widget=forms.Select(attrs={'class': 'form-control'}),
                                    choices=Customer.PRICE_CHOICES)
    warehouse = forms.ModelChoiceField(label=_('Warehouse'), queryset=Warehouse.objects.all(), required=False,
                                       widget=forms.Select(attrs={'class': 'form-control'}))
    salutation = forms.ChoiceField(label=_('Salutation'), required=True, choices=SALUTATION_CHOICES,
                                   widget=forms.Select(attrs={'class': 'form-control', 'placeholder': _('Salutation')}))

    class Meta:
        model = Customer

        fields = ["perm_street", "perm_pin", "perm_place", "perm_country", "diff_invoice_recipient", "company",
                  "cost_centre", "salutation", "addition1", "addition2", "addition3", "post_office_box", "name1",
                  "name2",
                  "description", "street", "pin", "fax", "place", "country",
                  "website", "contact_person1_email", "contact_person2_email", "contact_person3_email",
                  "contact_person1_phone", "contact_person2_phone", "contact_person3_phone", "customer_type",
                  "private_person", "document_lock", "payment_block", "delivery_terms", "special_discount",
                  "debitor_number", "dunning",
                  "price_group", "classification", "sector", "company_size", "area", "warehouse"]
        labels = {
            'name2': _("Name 2"),
            'name1': _("Name 1"),
            'street': _("Street"),
            'pin': _("Pin"),
            'description': _("Description"),
            'fax': _("Fax"),
            'place': _("Place"),
            'country': _("Country"),
            'company': _("Company"),
            'addition1': _("addition1"),
            'addition2': _("addition2"),
            'addition3': _("addition3"),
            # 'email': _("Email"),
            'website': _("Website"),
            'contact_person1_email': _("Email1"),
            'contact_person2_email': _("Email2"),
            'contact_person3_email': _("Email3"),
            'contact_person1_phone': _("Phone1"),
            'contact_person2_phone': _("Phone2"),
            'contact_person3_phone': _("Phone3"),
            'diff_invoice_recipient': _("Invoice Recipient"),
            'customer_type': _("Customer Type"),
            'classification': _("Classification"),
            'sector': _("Sector"),
            'company_size': _("Company Size"),
            'area': _("Area"),
            'private_person': _("Private Person"),
            'document_lock': _("Document Lock"),
            'payment_block': _("Payment Block"),
            'special_discount': _("Special Discount"),
            'debitor_number': _("Debitor Number"),
            'dunning': _("Dunning"),
            'cost_centre': _("Cost Centre"),
            'perm_street': _("Permenant Street"),
            'perm_pin': _("Permanent Pin"),
            'perm_place': _("Permanent Place"),
            'perm_country': _("Permanent Country"),
            'post_office_box': _("Post Box"),

        }


class SupplierForm(forms.ModelForm):
    first_name = forms.CharField(label=_("First Name"), required=False,
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    supplier_name = forms.CharField(label=_("Company"), widget=forms.TextInput(attrs={'class': 'form-control'}))
    name = forms.CharField(label=_("Surname"), required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    street = forms.CharField(label=_("Street"), required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    pin = forms.IntegerField(label=_("Pin"), required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    fax = forms.CharField(label=_("Fax"), required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    place = forms.CharField(label=_("Place"), required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    salutation = forms.ChoiceField(label=_('Salutation'), required=True, choices=SALUTATION_CHOICES,
                                   widget=forms.Select(attrs={'class': 'form-control', 'placeholder': _('Salutation')}))
    addition1 = forms.CharField(label=_("addition1"), required=False,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    addition2 = forms.CharField(label=_("addition2"), required=False,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    addition3 = forms.CharField(label=_("addition3"), required=False,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    post_office_box = forms.CharField(label=_("Post Box"), required=False,
                                      widget=forms.TextInput(attrs={'class': 'form-control'}))
    country = forms.CharField(label=_("Country"), required=False,
                              widget=forms.TextInput(attrs={'class': 'form-control'}))
    contact_person1_email = forms.CharField(label=_("Email1"), required=False,
                                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    contact_person2_email = forms.CharField(label=_("Email2"), required=False,
                                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    contact_person3_email = forms.CharField(label=_("Email3"), required=False,
                                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    contact_person1_phone = forms.CharField(label=_("Phone1"), required=False,
                                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    contact_person2_phone = forms.CharField(label=_("Phone2"), required=False,
                                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    contact_person3_phone = forms.CharField(label=_("Phone3"), required=False,
                                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    website = forms.CharField(label=_("Website"), required=False,
                              widget=forms.TextInput(attrs={'class': 'form-control'}))
    cost_centre = forms.IntegerField(label=_("Cost Centre"), required=False,
                                     widget=forms.NumberInput(attrs={'class': 'form-control'}))
    warehouse = forms.ModelChoiceField(label=_("Warehouse"), queryset=Warehouse.objects.all(), required=False,
                                       widget=forms.Select(attrs={'class': 'form-control'}))
    creditor_number = forms.IntegerField(label=_("Creditor number"), required=False,
                                         widget=forms.NumberInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Supplier

        fields = ["first_name", "supplier_name", "name", "street", "pin", "fax", "place", "salutation", "addition1",
                  "addition2", "addition3", "post_office_box", "country", "contact_person1_email",
                  "contact_person2_email",
                  "contact_person3_email", "contact_person1_phone", "contact_person2_phone", "contact_person3_phone",
                  "website", "cost_centre", "warehouse", "creditor_number"]
        # labels = {
        #     'short_name': _("Short name"),
        #     'supplier_name': _("Supplier name"),
        #     'name': _("Name"),
        #     'street': _("Street"),
        #     'pin': _("Pin"),
        #     'telephone': _("Telephone"),
        #     'place': _("Place"),
        #     'infotext': _("Infotext"),
        # }


class ForwardersForm(forms.ModelForm):
    second_name = forms.CharField(label=_("Surname"), required=False,
                                  widget=forms.TextInput(attrs={'class': 'form-control'}))
    name = forms.CharField(label=_("Company"), widget=forms.TextInput(attrs={'class': 'form-control'}))
    firstname = forms.CharField(label=_("First name"), required=False,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    street = forms.CharField(label=_("Street"), required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    pin = forms.CharField(label=_("Pin"), required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    telephone = forms.CharField(label=_("Telephone"), required=False,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    place = forms.CharField(label=_("Place"), required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # contact_person = forms.CharField(label=_("Contact person"), widget=forms.TextInput(attrs={'class': 'form-control'}))
    country = forms.CharField(label=_("Country"), required=False,
                              widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Forwarders

        fields = ["name", "firstname", "second_name", "street", "pin", "telephone", "place", "country"]
        # labels = {
        #     'short_name': "Short name",
        #     'name': "Name",
        #     'firstname': "First name",
        #     'street': "Street",
        #     'pin': "Pin",
        #     'telephone': "Telephone",
        #     'place': "Place",
        #     'contact_person': "Contact person",
        # }


class TransactionForm(forms.ModelForm):
    vehicle = forms.ModelChoiceField(label=_("License Plate"), queryset=Vehicle.objects.all(), required=False,
                                     widget=forms.Select(attrs={'class': 'form-control'}))
    article = forms.ModelChoiceField(label=_("Material"), queryset=Article.objects.all(), required=False,
                                     widget=forms.Select(attrs={'class': 'form-control'}))
    customer = forms.ModelChoiceField(label=_("Customer"), queryset=Customer.objects.all(), required=False,
                                      widget=forms.Select(
                                          attrs={'class': 'form-control', 'id': 'id_delivery_customer'}))
    supplier = forms.ModelChoiceField(label=_("Supplier"), queryset=Supplier.objects.all(), required=False,
                                      widget=forms.Select(attrs={'class': 'form-control'}))
    container = forms.ModelChoiceField(label=_("Container"), queryset=Container.objects.all(), required=False,
                                       widget=forms.Select(attrs={'class': 'form-control'}))
    total_price = forms.DecimalField(label=_('Total_price'), required=False)

    class Meta:
        model = Transaction

        fields = ["vehicle", "article", "customer", "supplier", "container", "first_weight", "second_weight",
                  "net_weight",
                  "firstw_alibi_nr",
                  "firstw_date_time", "secondw_alibi_nr", "secondw_date_time", "vehicle_weight_flag",
                  "vehicle_second_weight_flag", "trans_flag", "price_per_item", 'total_price']
        labels = {
            'first_weight': _("First Weight"),
            'net_weight': _("Net Weight"),
            'second_weight': _("Second Weight"),
            'secondw_alibi_nr': _("Alibi Nr"),
        }


class yardListForm(forms.ModelForm):
    class Meta:
        model = Yard_list

        fields = ["name", "place", "country"]
        labels = {
            'name': _("Name"),
            'place': _("Place"),
            'country': _("Country"),
        }


class ArticleForm(forms.ModelForm):
    group = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),
                              choices=Article.GROUP_CHOICES, label=_("Type"))

    revenue_group = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),
                                      choices=Article.REVENUE_GROUP_CHOICES, label=_("Revenue Group"), required=False)
    description = forms.CharField(label=_("Description"), widget=forms.Textarea(attrs={'class': 'form-control'}),
                                  required=False)
    ware_house = forms.ModelChoiceField(label=_("Warehouse"), required=False, queryset=Warehouse.objects.all(),
                                        widget=forms.Select(attrs={'class': 'form-control'}))
    supplier = forms.ModelChoiceField(label=_("Supplier"), queryset=Supplier.objects.all(), required=False,
                                      widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Article

        fields = ["supplier", "name", "description", "short_name", "group", "vat", "minimum_amount", "price1", "price2",
                  "price3", "price4", "price5", "discount", "avv_num", "account", "cost_center", "unit", "min_quantity",
                  "revenue_group", "revenue_account", "list_price_net", "ean", "ware_house"]
        labels = {
            'name': _("Name"),
            'short_name': _("Short Name"),
            'vat': _("Vat"),
            'minimum_amount': _("Minimum Amount"),
            'price1': _("Price 1"),
            'price2': _("Price 2"),
            'price3': _("Price 3"),
            'price4': _("Price 4"),
            'price5': _("Price 5"),
            'discount': _("Discount"),
            'avv_num': _("Avv Num"),
            'account': _("Account"),
            'cost_center': _("Cost Centre"),
            'unit': _("Unit"),
            'min_quantity': _("Min Quantity"),
            'revenue_account': _("Revenue Account"),
            'list_price_net': _("List Price Net"),
            'ean': _("EAN"),
            'avv_num': _("Avv-Number")
        }


class BuildingSiteForm(forms.ModelForm):
    class Meta:
        model = BuildingSite

        fields = ["name", "short_name", "place", "street", "pin", "infotext"]
        labels = {
            'name': _("Name"),
            'short_name': _("Short Name"),
            'place': _("Place"),
            'street': _("Street"),
            'pin': _("Pin"),
            'infotext': _("Infotext"),
        }


class Delivery_noteForm(forms.ModelForm):
    class Meta:
        model = Delivery_note

        fields = ["lfd_nr", "file_name"]
        labels = {
            'lfd_nr': _("Lfd Nr"),
            'file_name': _("File Name"),
        }


class VehicleForm(forms.ModelForm):
    license_plate = forms.CharField(label=_("License Plate"), widget=forms.TextInput(attrs={'class': 'form-control'}))
    license_plate2 = forms.CharField(label=_("License Plate 2"), required=False,
                                     widget=forms.TextInput(attrs={'class': 'form-control'}))
    # forwarder = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    vehicle_weight_date = forms.DateField(label=_("Weight Date"), required=False,
                                          widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    vehicle_weight_time = forms.TimeField(label=_("Weight Time"), required=False,
                                          widget=forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}))

    forwarder = forms.ModelChoiceField(label=_("Forwarder"), queryset=Forwarders.objects.all(), required=False,
                                       widget=forms.Select(attrs={'class': 'form-control'}))
    group = forms.IntegerField(label=_("Group"), required=False,
                               widget=forms.NumberInput(attrs={'class': 'form-control'}))
    country = forms.CharField(label=_("Country"), required=False,
                              widget=forms.TextInput(attrs={'class': 'form-control'}))
    telephone = forms.CharField(label=_("Telephone"), required=False,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    vehicle_weight = forms.IntegerField(label=_("Vehicle Weight"), required=False,
                                        widget=forms.NumberInput(attrs={'class': 'form-control'}))
    vehicle_weight2 = forms.IntegerField(label=_("Vehicle Weight 2"), required=False,
                                         widget=forms.NumberInput(attrs={'class': 'form-control'}))
    vehicle_weight_id = forms.CharField(label=_("Vehicle Weight Id"), required=False,
                                        widget=forms.TextInput(attrs={'class': 'form-control'}))
    vehicle_type = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),
                                     choices=Vehicle.VEHICLE_CHOICES, label=_("Type"), required=False)

    class Meta:
        model = Vehicle

        fields = ["license_plate", "forwarder", "group", "country", "telephone", "vehicle_weight", "vehicle_weight2",
                  "vehicle_weight_id", "vehicle_weight_date", "vehicle_weight_time", "taken", "license_plate2",
                  "vehicle_type", "cost_center", "owner", "driver_name", "trailor_weight"]
        labels = {
            'taken': _("Taken"),
            'cost_center': _("Cost Centre"),
            'owner': _("Vehicle Owner"),
            'driver_name': _("Driver"),
            'trailor_weight': _("Trailor Weight"),
        }


class CombinationForm(forms.ModelForm):
    class Meta:
        model = Combination

        fields = ["ident", "customer", "vehicle", "supplier", "article", "container", "transaction_id"]


class SettingsForm(forms.ModelForm):
    customer = forms.ChoiceField(label=_("Customer"), widget=forms.RadioSelect(attrs={'class': 'form-radio'}),
                                 required=False, choices=Settings.CUSTOMER_CHOICES)
    supplier = forms.ChoiceField(label=_("Supplier"), widget=forms.RadioSelect(attrs={'class': 'form-radio'}),
                                 required=False, choices=Settings.SUPPLIER_CHOICES)
    article = forms.ChoiceField(label=_("Article"), widget=forms.RadioSelect(attrs={'class': 'form-radio'}),
                                required=False, choices=Settings.ARTICLE_CHOICES)

    class Meta:
        model = Settings
        # fields = ["name","customer","article","supplier","show_article","show_supplier","show_yard","show_forwarders","show_storage","show_building_site","read_number_from_camera","language"]
        fields = ["name", "customer", "article", "supplier", "language", "smtp_support", "smtp_creds", "company_email"]
        # labels = {"read_number_from_camera":"Read Number plate from camera"}

        labels = {
            'name': _("Name"),
            'language': _("Language"),
            'article': _("Article"),
            'company_email': _("Company Email")
        }


class SmtpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = SMTPCred
        fields = ["host", "port", "username", "password", "sender_address"]


class ContainerForm(forms.ModelForm):
    name = forms.CharField(label=_("Name"), widget=forms.TextInput(attrs={'class': 'form-control'}))
    group = forms.IntegerField(label=_("Group"), widget=forms.NumberInput(attrs={'class': 'form-control'}))

    # last_site = forms.ModelChoiceField(queryset=BuildingSite.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    class Meta:
        model = Container

        fields = ["name", "container_type", "group", "container_weight", "volume", "container_number",
                  "maximum_gross_weight", "tare_weight", "payload_container_volume", "next_exam", "waste_type",
                  "hazard_warnings"]
        labels = {
            'container_type': _("Container Type"),
            'container_weight': _("Container Weight"),
            'volume': _("Volume"),
            'container_number': _("Container number"),
            'maximum_gross_weight': _("Maximum gross weight"),
            'tare_weight': _("Tare weight"),
            'payload_container_volume': _("Payload container volume"),
            'next_exam': _("Next exam"),
            'waste_type': _("Waste type"),
            'hazard_warnings': _("Hazard warnings")
        }


class SSUpdateForm(forms.Form):
    field_type = forms.CharField()
    user = forms.IntegerField()
    values = SimpleArrayField(forms.IntegerField(), required=False)


class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = ["contract_number", "customer",
                  "start_date", "end_date",
                  "vehicles", "construction_site", "signature"]


class WarehouseForm(forms.ModelForm):
    class Meta:
        model = Warehouse

        fields = ["name", "stock_designation", "stock_number", "stock_item", "locked_warehouse", "ordered",
                  "production", "reserved", "available", "total_stock", "store", "outsource", "storage_location",
                  "warehouse_street", "minimum_quantity"]

        labels = {
            'name': _("Name"),
            'stock_designation': _("Stock Designation"),
            'stock_number': _("Stock Number"),
            'stock_item': _("Stock Item"),
            'locked_warehouse': _("Locked Warehouse"),
            'ordered': _("Ordered"),
            'production': _("Production"),
            'reserved': _("Reserved"),
            'available': _("Available"),
            'total_stock': _("Total Stock"),
            'store': _("Store"),
            'outsource': _("Outsource"),
            'storage_location': _("Storage location"),
            'warehouse_street': _("Warehouse street"),
            'minimum_quantity': _("Minimum quantity"),
        }


class SiloForm(forms.ModelForm):
    supplier = forms.ModelChoiceField(label=_("Supplier"), queryset=Supplier.objects.all(), required=False,
                                     widget=forms.Select(attrs={'class': 'form-control'}))
    warehouse = forms.ModelChoiceField(label=_("Warehouse"), queryset=Warehouse.objects.all(), required=False,
                                     widget=forms.Select(attrs={'class': 'form-control'}))
    class Meta:
        model = Silo
        fields = ['name','warehouse','supplier','capacity']

class MaterialQualityForm(forms.ModelForm):
    quality = forms.ChoiceField(choices=MaterialQuality.QUALITY_CHOICES, widget=forms.Select(attrs={"class":"form-control"}))
    humidity = forms.ChoiceField(choices=MaterialQuality.HUMIDITY_CHOICES, widget=forms.Select(attrs={"class":"form-control"}))
    fertilizer = forms.ChoiceField(choices=MaterialQuality.FERTILIZER_CHOICES, widget=forms.Select(attrs={"class":"form-control"}))
    class Meta:
        model = MaterialQuality
        fields = '__all__'