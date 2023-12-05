import uuid
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _

from django.core.validators import MinValueValidator

from .managers import UserManager

SALUTATION_CHOICES = (
    (_('Mr'), _('Mr')),
    (_('Mrs'), _('Mrs')),
    (_('Company'), _('Company')),
)


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(_('name'), max_length=30, blank=True)
    email = models.EmailField(_('email address'), unique=True)
    # password = models.CharField(_('password'),max_length=100)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff status'), default=True)
    # yard_id = models.CharField(_('yard ID'), max_length=30,)
    yard = models.ForeignKey('Yard_list', on_delete=models.CASCADE, null=True)
    role = models.CharField(_('role'), max_length=30, blank=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    telephone = models.CharField(max_length=20, blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
    # class Meta:
    #     verbose_name = _('user')
    #     verbose_name_plural = _('users')

    # def get_full_name(self):
    #     '''
    #     Returns the first_name plus the last_name, with a space in between.
    #     '''
    #     full_name = '%s %s' % (self.first_name, self.last_name)
    #     return full_name.strip()


class Signature(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    signature = models.FileField(upload_to='signatures/', null=True)


class images_base64(models.Model):
    """docstring for images_base64"""
    transaction = models.ForeignKey('Transaction', on_delete=models.CASCADE, null=True)
    image1 = models.ImageField(null=True)
    image2 = models.ImageField(null=True)
    image3 = models.ImageField(null=True)


class Article(models.Model):
    GROUP_CHOICES = (
        (1, _('Type 1')),
        (2, _('Type 2')),
        (3, _('Type 3')),
        (4, _('Type 4')),
        (5, _('Type 5')),
        (6, _('Other Type')),)
    REVENUE_GROUP_CHOICES = (
        ('revenue1', _('Revenue 1')),
        ('revenue2', _('Revenue 2')),
        ('revenue3', _('Revenue 3')),
        ('revenue4', _('Revenue 4')),
        ('revenue5', _('Revenue 5')),
    )

    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    short_name = models.CharField(max_length=40, blank=True, null=True)
    yard = models.ForeignKey('Yard_list', on_delete=models.CASCADE, blank=True, null=True)
    entry_weight = models.DecimalField(max_digits=10, decimal_places=4, default=0.0,
                                       validators=[MinValueValidator(0.0)], blank=True, null=True)
    balance_weight = models.DecimalField(max_digits=10, decimal_places=2, default=0.0,
                                         validators=[MinValueValidator(0.0)], blank=True, null=True)
    outgoing_weight = models.DecimalField(max_digits=10, decimal_places=2, default=0.0,
                                          validators=[MinValueValidator(0.0)], blank=True, null=True)
    # entry_weight = models.IntegerField(null=True, blank=True)
    # balance_weight = models.IntegerField(null=True, blank=True)
    # outgoing_weight = models.IntegerField(null=True, blank=True)
    price1 = models.IntegerField(null=True, blank=True)
    # price1 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    price2 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    price3 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    price4 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    price5 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    discount = models.CharField(max_length=100, blank=True, null=True)
    group = models.PositiveIntegerField(choices=GROUP_CHOICES, default=6, blank=True, null=True)
    vat = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    minimum_amount = models.IntegerField(null=True, blank=True, default=0)
    # minimum_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    created_date_time = models.DateTimeField(auto_now_add=True, blank=True)
    updated_date_time = models.DateTimeField(auto_now=True, blank=True)

    avv_num = models.CharField(max_length=250, blank=True, null=True)
    account = models.CharField(max_length=250, blank=True, null=True)
    cost_center = models.CharField(max_length=250, blank=True, null=True)
    unit = models.CharField(max_length=250, blank=True, null=True)
    min_quantity = models.PositiveIntegerField(blank=True, null=True)
    revenue_group = models.CharField(max_length=250, choices=REVENUE_GROUP_CHOICES, blank=True, null=True)
    revenue_account = models.CharField(max_length=250, blank=True, null=True)
    list_price_net = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    ean = models.CharField(max_length=250, blank=True, null=True)
    ware_house = models.ForeignKey('Warehouse', on_delete=models.CASCADE, blank=True, null=True)
    supplier = models.ForeignKey('Supplier', on_delete=models.CASCADE, null=True)
    ss_role_access = models.ManyToManyField('yard.User', blank=True, null=True)

    class Meta:
        ordering = ('name',)
        unique_together = ('name', 'yard',)

    def __str__(self):
        return self.name


class Article_meta(models.Model):
    article = models.ForeignKey('Article', on_delete=models.CASCADE, null=True)
    yard = models.ForeignKey('Yard_list', on_delete=models.CASCADE)
    entry_weight = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    balance_weight = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    outgoing_weight = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)

    class Meta:
        unique_together = ('article', 'yard',)

    def __str__(self):
        return self.balance_weight


class BuildingSite(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    short_name = models.CharField(max_length=40, blank=True, null=True)
    place = models.CharField(max_length=100, blank=True, null=True)
    street = models.CharField(max_length=100, blank=True, null=True)
    pin = models.CharField(max_length=100, blank=True, null=True)
    infotext = models.CharField(max_length=100, blank=True)
    created_date_time = models.DateTimeField(auto_now_add=True, blank=True)
    updated_date_time = models.DateTimeField(auto_now=True, blank=True)
    ss_role_access = models.ManyToManyField('yard.User')

    def __str__(self):
        return self.name


class Delivery_note(models.Model):
    lfd_nr = models.CharField(max_length=100)
    file_name = models.CharField(max_length=100)
    created_date_time = models.DateTimeField(auto_now_add=True, blank=True)
    updated_date_time = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.lfd_nr


class Vehicle(models.Model):
    VEHICLE_CHOICES = (
        ('type1', _('Type 1')),
        ('type2', _('Type 2')),
        ('type3', _('Type 3')),
        ('type4', _('Type 4')),
        ('type5', _('Type 5')),)
    license_plate = models.CharField(max_length=100, null=True, unique=True)
    license_plate2 = models.CharField(max_length=100, blank=True, null=True)
    forwarder = models.ForeignKey('Forwarders', on_delete=models.CASCADE, null=True)
    group = models.PositiveIntegerField(null=True, blank=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    telephone = models.CharField(max_length=20, blank=True, null=True)
    # vehicle_weight = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    vehicle_weight = models.IntegerField(blank=True, null=True, default=0)
    vehicle_weight2 = models.IntegerField(blank=True, null=True, default=0)
    # vehicle_weight2 = models.DecimalField(max_digits=10, decimal_places=0, default=0, blank=True, null=True)
    vehicle_weight_id = models.CharField(max_length=100, blank=True, null=True)
    vehicle_weight_date = models.DateField(blank=True, null=True)
    vehicle_weight_time = models.TimeField(blank=True, null=True)
    taken = models.PositiveIntegerField(null=True, blank=True)
    created_date_time = models.DateTimeField(auto_now_add=True, blank=True)
    updated_date_time = models.DateTimeField(auto_now=True, blank=True)
    vehicle_type = models.CharField(max_length=10, choices=VEHICLE_CHOICES, null=True, blank=True)
    cost_center = models.CharField(max_length=100, blank=True, null=True)
    owner = models.CharField(max_length=100, blank=True, null=True)
    driver_name = models.CharField(max_length=100, blank=True, null=True)
    trailor_weight = models.DecimalField(max_digits=10, decimal_places=0, default=0, null=True)
    ss_role_access = models.ManyToManyField('yard.User', blank=True, null=True)

    def __str__(self):
        return self.license_plate

    class Meta:
        ordering = ('license_plate',)


class Combination(models.Model):  # Kombinationen
    ident = models.CharField(max_length=40, unique=True)
    short_name = models.CharField(max_length=40, blank=True, null=True)  # kurezel
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE, null=True, blank=True)
    vehicle = models.ForeignKey('Vehicle', on_delete=models.CASCADE, null=True, blank=True)
    building_site = models.ForeignKey('BuildingSite', on_delete=models.CASCADE, null=True, blank=True)
    supplier = models.ForeignKey('Supplier', on_delete=models.CASCADE, null=True, blank=True)
    forwarders = models.ForeignKey('Forwarders', on_delete=models.CASCADE, null=True, blank=True)  # spediteure
    article = models.ForeignKey('Article', on_delete=models.CASCADE, null=True, blank=True)
    yard = models.ForeignKey('Yard_list', on_delete=models.CASCADE, null=True, blank=True)
    container = models.ForeignKey('Container', on_delete=models.CASCADE, null=True, blank=True)
    transaction_id = models.ForeignKey('Transaction', on_delete=models.CASCADE, null=True, blank=True)
    created_date_time = models.DateTimeField(auto_now_add=True, blank=True)
    updated_date_time = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.ident


class Customer(models.Model):  # Kunden

    PRICE_CHOICES = (
        ('price1', _('Price 1')),
        ('price2', _('Price 2')),
        ('price3', _('Price 3')),
        ('price4', _('Price 4')),
        ('price5', _('Price 5')),
    )
    DELIVERY_CHOICES = (
        ('free', _('Free')),
        ('paid', _('Paid')),
        ('other', _('Other')),
    )
    name1 = models.CharField(max_length=40, unique=True)
    name2 = models.CharField(max_length=40, blank=True, null=True)  # vorname
    company = models.CharField(max_length=40, blank=True, null=True)
    salutation = models.CharField(max_length=10, choices=SALUTATION_CHOICES, blank=True, null=True)
    addition1 = models.CharField(max_length=40, blank=True, null=True)
    addition2 = models.CharField(max_length=40, blank=True, null=True)
    addition3 = models.CharField(max_length=40, blank=True, null=True)
    post_office_box = models.CharField(max_length=40, blank=True, null=True)
    description = models.CharField(max_length=250, blank=True, null=True)  # bezeichnung
    street = models.CharField(max_length=250, blank=True, null=True)  # strasse
    pin = models.CharField(max_length=10, blank=True, null=True)
    fax = models.CharField(max_length=15, blank=True, null=True)
    place = models.CharField(max_length=100, blank=True, null=True)
    website = models.CharField(max_length=100, blank=True, null=True)
    cost_centre = models.PositiveIntegerField(null=True, default=1)  # kostenstelle
    country = models.CharField(max_length=100, blank=True, null=True)
    # email = models.CharField(max_length=40, blankHi M=True, null=True)
    contact_person1_email = models.CharField(max_length=40, blank=True, null=True)
    contact_person2_email = models.CharField(max_length=40, blank=True, null=True)
    contact_person3_email = models.CharField(max_length=40, blank=True, null=True)
    contact_person1_phone = models.CharField(max_length=40, blank=True, null=True)
    contact_person2_phone = models.CharField(max_length=40, blank=True, null=True)
    contact_person3_phone = models.CharField(max_length=40, blank=True, null=True)
    diff_invoice_recipient = models.CharField(max_length=40, blank=True, null=True)
    customer_type = models.CharField(max_length=40, blank=True, null=True)
    price_group = models.CharField(max_length=10, choices=PRICE_CHOICES, blank=True, null=True)
    classification = models.CharField(max_length=40, blank=True, null=True)
    sector = models.CharField(max_length=40, blank=True, null=True)
    company_size = models.CharField(max_length=40, blank=True, null=True)
    area = models.CharField(max_length=40, blank=True, null=True)
    warehouse = models.ForeignKey('Warehouse', on_delete=models.CASCADE, null=True)
    private_person = models.BooleanField(default=False)
    document_lock = models.BooleanField(default=False)
    payment_block = models.BooleanField(default=False)
    delivery_terms = models.CharField(max_length=10, choices=DELIVERY_CHOICES, blank=True, null=True)
    special_discount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    debitor_number = models.PositiveIntegerField(null=True, blank=True)  # kostenstelle
    dunning = models.CharField(max_length=10, null=True, blank=True)
    perm_street = models.CharField(max_length=100, blank=True, null=True)  # strasse
    perm_pin = models.CharField(max_length=10, blank=True, null=True)
    perm_place = models.CharField(max_length=100, blank=True, null=True)
    perm_country = models.CharField(max_length=100, blank=True, null=True)
    ss_role_access = models.ManyToManyField('yard.User', blank=True, null=True)
    created_date_time = models.DateTimeField(auto_now_add=True, blank=True)
    updated_date_time = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.name1

    class Meta:
        ordering = ('name1',)


class Supplier(models.Model):  # Lieferanten

    supplier_name = models.CharField(max_length=100, unique=True)  # Lieferanten_name
    name = models.CharField(max_length=40, blank=True, null=True)
    first_name = models.CharField(max_length=40, blank=True, null=True)  # kurezel
    street = models.CharField(max_length=100, blank=True, null=True)  # strasse
    pin = models.CharField(max_length=10, blank=True, null=True)
    fax = models.CharField(max_length=15, blank=True, null=True)
    place = models.CharField(max_length=100, blank=True, null=True)
    infotext = models.CharField(max_length=100, blank=True, null=True)
    salutation = models.CharField(max_length=10, choices=SALUTATION_CHOICES, blank=True, null=True)
    addition1 = models.CharField(max_length=40, blank=True, null=True)
    addition2 = models.CharField(max_length=40, blank=True, null=True)
    addition3 = models.CharField(max_length=40, blank=True, null=True)
    post_office_box = models.CharField(max_length=40, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    contact_person1_email = models.CharField(max_length=40, blank=True, null=True)
    contact_person2_email = models.CharField(max_length=40, blank=True, null=True)
    contact_person3_email = models.CharField(max_length=40, blank=True, null=True)
    contact_person1_phone = models.CharField(max_length=40, blank=True, null=True)
    contact_person2_phone = models.CharField(max_length=40, blank=True, null=True)
    contact_person3_phone = models.CharField(max_length=40, blank=True, null=True)
    website = models.CharField(max_length=100, blank=True, null=True)
    cost_centre = models.PositiveIntegerField(null=True, default=1)
    warehouse = models.ForeignKey('Warehouse', on_delete=models.CASCADE, null=True)
    creditor_number = models.PositiveIntegerField(null=True, blank=True)
    ss_role_access = models.ManyToManyField('yard.User')
    created_date_time = models.DateTimeField(auto_now_add=True, blank=True)
    updated_date_time = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.supplier_name

    class Meta:
        ordering = ('supplier_name',)


class Forwarders(models.Model):  # Spediteure
    name = models.CharField(max_length=100, unique=True)
    firstname = models.CharField(max_length=100, blank=True, null=True)  # vorname
    second_name = models.CharField(max_length=100, blank=True, null=True)
    street = models.CharField(max_length=100, blank=True, null=True)  # strasse
    pin = models.CharField(max_length=10, blank=True, null=True)  # plz
    telephone = models.CharField(max_length=15, blank=True, null=True)  # telefon
    place = models.CharField(max_length=100, blank=True, null=True)  # ort
    country = models.CharField(max_length=100, blank=True, null=True)  # ort
    contact_person = models.CharField(max_length=100, blank=True, null=True)  # ansprech_partner
    created_date_time = models.DateTimeField(auto_now_add=True, blank=True)
    updated_date_time = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    TRANS_CHOICES = (
        (0, 'Initial_Weighing'),
        (1, 'Second_Weighing'),
        (2, 'Closed_Weighing'),
    )
    vehicle = models.ForeignKey('Vehicle', on_delete=models.CASCADE, null=True, blank=True)
    article = models.ForeignKey('Article', on_delete=models.CASCADE, null=True, blank=True)
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE, null=True, blank=True)
    supplier = models.ForeignKey('Supplier', on_delete=models.CASCADE, null=True, blank=True)
    container = models.ForeignKey('Container', on_delete=models.CASCADE, null=True, blank=True)
    yard = models.ForeignKey('Yard_list', on_delete=models.CASCADE, null=True, blank=True)
    combination_id = models.CharField(max_length=10, blank=True, null=True)
    first_weight = models.DecimalField(max_digits=10, decimal_places=0, default=0, null=True)
    second_weight = models.DecimalField(max_digits=10, decimal_places=0, default=0, null=True)
    net_weight = models.DecimalField(max_digits=10, decimal_places=0, default=0, null=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=0, null=True, blank=True)
    lfd_nr = models.CharField(max_length=40, null=True, blank=True)
    firstw_date_time = models.DateTimeField(blank=True, null=True)
    secondw_date_time = models.DateTimeField(blank=True, null=True)
    firstw_alibi_nr = models.CharField(max_length=40, null=True, blank=True)
    secondw_alibi_nr = models.CharField(max_length=40, null=True, blank=True)
    vehicle_weight_flag = models.IntegerField(default=0, blank=True, null=True)
    vehicle_second_weight_flag = models.IntegerField(default=0, blank=True, null=True)
    created_date_time = models.DateTimeField(auto_now_add=True, blank=True)
    updated_date_time = models.DateTimeField(auto_now=True, blank=True)
    trans_flag = models.PositiveIntegerField(null=True, choices=TRANS_CHOICES)
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=00, blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    contract_number = models.ForeignKey("yard.Contract", on_delete=models.CASCADE, blank=True, null=True)

    def get_context_transaction(self, request):
        context = {}
        context["absolute_url"] = "http://" + request.get_host()
        context['logo'] = Logo.objects.all()
        context['role'] = request.user.role
        context['user_name'] = request.user.name
        context['sign'] = Signature.objects.filter(user=request.user).last()
        context["dataset"] = self
        context["images"] = self.images_base64_set.first()
        return context

    def __str__(self):
        return str(self.lfd_nr) if self.lfd_nr else ''


class Yard_list(models.Model):
    # license_plate = models.CharField(max_length=100, null=True, blank=True)#kennung
    # vehicle_weight = models.PositiveIntegerField(blank=True, null=True)#tara
    # vehicle_weight_id = models.CharField(max_length=100, null=True, blank=True)#tara_id
    # created_date_time = models.DateTimeField(auto_now_add=True, blank=True)
    # updated_date_time = models.DateTimeField(auto_now=True, blank=True)
    name = models.CharField(max_length=100, unique=True)
    street = models.CharField(max_length=40, blank=True, null=True)
    pin = models.CharField(max_length=10, blank=True, null=True)
    place = models.CharField(max_length=40, blank=True, null=True)
    country = models.CharField(max_length=40, blank=True, null=True)
    telephone = models.CharField(max_length=15, blank=True, null=True)
    email = models.CharField(max_length=40, blank=True, null=True)
    created_date_time = models.DateTimeField(auto_now_add=True, blank=True)
    updated_date_time = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.name


class Settings(models.Model):
    CUSTOMER_CHOICES = (
        ('Kunde', 'Kunde'),
        ('Erzeuger', 'Erzeuger'),
        # ('Customer', 'Customer'),
    )  # KUNDE_CHOICES
    SUPPLIER_CHOICES = (
        ('Lieferant', 'Lieferant'),
        ('Baustelle', 'Baustelle'),
        ('Schlag', 'Schlag'),
        # ('Supplier', 'Supplier'),
    )  # LIEFERANT_CHOICES
    ARTICLE_CHOICES = (
        ('Material', 'Material'),
        ('Produkt', 'Produkt'),
        # ('kultur', 'Kultur'),
        ('Artikel', 'Artikel'),
        # ('Article', 'Article'),
    )
    LANGUAGE_CHOICES = (
        # ('en-us', 'English'),
        ('de', 'Deutsch'),
        ('fr', 'French'),
        ('ru', 'Russian'),
    )
    name = models.CharField(max_length=40, blank=True, null=True, unique=True)
    customer = models.CharField(max_length=40, null=True, choices=CUSTOMER_CHOICES)  # kunde
    supplier = models.CharField(max_length=40, null=True, choices=SUPPLIER_CHOICES)  # lieferant
    article = models.CharField(max_length=40, null=True, choices=ARTICLE_CHOICES)  # artikel
    show_article = models.BooleanField(default=True)  # show_artikel
    show_supplier = models.BooleanField(default=True)  # show_lieferant
    show_yard = models.BooleanField(default=True)
    show_forwarders = models.BooleanField(default=True)  # show_spediteure
    show_storage = models.BooleanField(default=True)
    show_building_site = models.BooleanField(default=True)  # show_baustellen
    company_email = models.EmailField(null=True, blank=True)
    yard = models.ForeignKey('Yard_list', on_delete=models.CASCADE)
    created_date_time = models.DateTimeField(auto_now_add=True, blank=True)
    updated_date_time = models.DateTimeField(auto_now=True, blank=True)
    read_number_from_camera = models.BooleanField(default=False)  # read_fahr_camera
    language = models.CharField(max_length=40, null=True, choices=LANGUAGE_CHOICES, default="en-us")  # LANGUAGE
    smtp_support = models.BooleanField(default=False)
    smtp_creds = models.ForeignKey('SMTPCred', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        # return self.identifier
        return self.name


class SMTPCred(models.Model):
    host = models.CharField(max_length=1000, unique=True)
    port = models.IntegerField()
    username = models.CharField(max_length=1000, unique=True)
    password = models.CharField(max_length=1000)
    sender_address = models.EmailField()


class Contract(models.Model):
    contract_number = models.CharField(max_length=1000, primary_key=True, unique=True)
    customer = models.ForeignKey("yard.Customer", on_delete=models.CASCADE)
    required_materials = models.JSONField(blank=False)
    vehicles = models.ManyToManyField("yard.Vehicle")
    construction_site = models.ManyToManyField("yard.BuildingSite", blank=True)
    signature = models.FileField(upload_to="contract_signatures/", blank=True)
    start_date = models.DateField(blank=False, null=False)
    end_date = models.DateField(blank=False, null=False)


class Container(models.Model):
    # license_plate = models.CharField(max_length=100, null=True, blank=True)#kennung
    # vehicle_weight = models.PositiveIntegerField(blank=True, null=True)#tara
    # vehicle_weight_id = models.CharField(max_length=100, null=True, blank=True)#tara_id
    # created_date_time = models.DateTimeField(auto_now_add=True, blank=True)
    # updated_date_time = models.DateTimeField(auto_now=True, blank=True)
    name = models.CharField(max_length=100, unique=True)
    container_type = models.CharField(max_length=40, blank=True, null=True)
    group = models.PositiveIntegerField(null=True, blank=True)
    container_weight = models.IntegerField(blank=True, default=0)
    volume = models.CharField(max_length=40, blank=True, null=True)
    last_site = models.ForeignKey('BuildingSite', on_delete=models.CASCADE, null=True)
    created_date_time = models.DateTimeField(auto_now_add=True, blank=True)
    updated_date_time = models.DateTimeField(auto_now=True, blank=True)
    # NEW DEMANDED FIELDS
    container_number = models.PositiveIntegerField(null=True, blank=True)
    maximum_gross_weight = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True)
    tare_weight = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True, null=True)
    payload_container_volume = models.CharField(max_length=40, null=True, blank=True)
    next_exam = models.DateField(blank=True, null=True)
    waste_type = models.CharField(max_length=50, blank=True, null=True)
    hazard_warnings = models.CharField(max_length=200, blank=True, null=True)
    ss_role_access = models.ManyToManyField('yard.User')

    def __str__(self):
        return self.name


class Warehouse(models.Model):
    name = models.CharField(max_length=100, unique=True)
    stock_designation = models.CharField(max_length=100, blank=True, null=True)
    stock_number = models.CharField(max_length=100, blank=True, null=True)
    stock_item = models.BooleanField(default=True)
    locked_warehouse = models.BooleanField(default=True)
    ordered = models.BooleanField(default=True)
    production = models.CharField(max_length=100, blank=True, null=True)
    reserved = models.CharField(max_length=100, blank=True, null=True)
    available = models.PositiveIntegerField(blank=True, null=True)
    total_stock = models.PositiveIntegerField(blank=True, null=True)
    store = models.PositiveIntegerField(blank=True, null=True)
    outsource = models.PositiveIntegerField(blank=True, null=True)
    created_date_time = models.DateTimeField(auto_now_add=True, blank=True)
    updated_date_time = models.DateTimeField(auto_now=True, blank=True)
    # NEW DEMANDED FIELDS
    storage_location = models.CharField(max_length=100, blank=True, null=True)
    warehouse_street = models.CharField(max_length=100, blank=True, null=True)
    minimum_quantity = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.name


class ForeignWeigh(models.Model):
    customer = models.CharField(max_length=100, blank=True, null=True)
    vehicle = models.CharField(max_length=100, blank=True, null=True)
    supplier = models.CharField(max_length=100, blank=True, null=True)
    article = models.CharField(max_length=100, blank=True, null=True)
    first_weight = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    second_weight = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    net_weight = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=0, null=True, blank=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    updated_date_time = models.DateTimeField(auto_now=True, blank=True)
    secondw_alibi_nr = models.CharField(max_length=100, blank=True, null=True)
    transaction_id = models.IntegerField(blank=True, null=True)


class Logo(models.Model):
    heading = models.TextField(max_length=1000, blank=True, null=True)
    logo = models.ImageField(upload_to="logo/", null=True)


class SelectCamera(models.Model):
    yes = models.BooleanField(default=True)
    number = models.IntegerField(default=1, blank=True, null=True)


class Barrier(models.Model):
    barrier = models.BooleanField(default=False)
    count = models.IntegerField(default=1, blank=True, null=True)


class TrafficLight(models.Model):
    status = models.BooleanField(default=False)


class PriceGroup(models.Model):
    status = models.BooleanField(default=False)


class ContainerShow(models.Model):
    status = models.BooleanField(default=False)


class ShowTonne(models.Model):
    status = models.BooleanField(default=False)


class Io(models.Model):
    status = models.BooleanField(default=False)


class ExternalWeigh(models.Model):
    status = models.BooleanField(default=False)


class ForeignFlag(models.Model):
    status = models.IntegerField(default=0)


class AutoCapture(models.Model):
    status = models.BooleanField(default=False)


class FirstWeightCameras(models.Model):
    cam1 = models.BooleanField(default=False)
    cam2 = models.BooleanField(default=False)
    cam3 = models.BooleanField(default=False)


class SecondWeightCameras(models.Model):
    cam1 = models.BooleanField(default=False)
    cam2 = models.BooleanField(default=False)
    cam3 = models.BooleanField(default=False)


class Silo(models.Model):
    name = models.CharField(max_length=100)
    warehouse = models.ForeignKey('Warehouse', on_delete=models.CASCADE, blank=True, null=True)
    supplier = models.ForeignKey('Supplier', on_delete=models.CASCADE, blank=True, null=True)
    capacity = models.IntegerField(blank=True, null=True)
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)



class MaterialQuality(models.Model):
    QUALITY_CHOICES = (('Quality A', 'Quality A'), ('Quality B', 'Quality B'), ('Quality C', 'Quality C'))
    HUMIDITY_CHOICES = (('Good', 'Good'), ('Average', 'Average'), ('Worse', 'Worse'))
    FERTILIZER_CHOICES = (('A Grade', 'A Grade'), ('B Grade', 'B Grade'), ('C Grade', 'C Grade'))
    
    material = models.ForeignKey('Article', on_delete=models.CASCADE)
    quality = models.CharField('quality', max_length=100, choices=QUALITY_CHOICES)
    humidity = models.CharField(max_length=100, choices=HUMIDITY_CHOICES)
    Fertilizer = models.CharField(max_length=100, choices=FERTILIZER_CHOICES)
    Amount = models.IntegerField(blank=True)
