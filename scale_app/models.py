from django.db import models

# Create your models here.
class Devices(models.Model):
    name = models.CharField(max_length=100, unique=True)
    ip_addr = models.CharField(max_length=100, blank=True, null=True)
    serial_num = models.CharField(max_length=100,default="None", null=True)
    mac_addr = models.CharField(max_length=100, null=True)
    port = models.PositiveIntegerField(null=True, blank=True)
    wx_btn = models.BooleanField(default=True)
    zero_btn = models.BooleanField(default=True)
    tara_btn = models.BooleanField(default=True)
    man_tara_btn = models.BooleanField(default=True)
    x10_btn = models.BooleanField(default=True)
    active = models.BooleanField(default=False)
    certi_num = models.CharField(max_length=100,default="None", null=True)
    max_weight = models.PositiveIntegerField(blank=True, null=True)
    min_weight = models.PositiveIntegerField(blank=True, null=True)
    e_d = models.PositiveIntegerField(null=True, blank=True,default=1)
    created_date_time = models.DateTimeField(auto_now_add=True, blank=True)
    updated_date_time = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self): 
        return self.name

class Transaction(models.Model):
    trans_id = models.AutoField(primary_key=True)
    device = models.ForeignKey('Devices',on_delete=models.CASCADE)
    created_date_time = models.DateTimeField(auto_now_add=True, blank=True)
    updated_date_time = models.DateTimeField(auto_now=True, blank=True)
    tara = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    net_weight = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    def __str__(self): 
        return self.trans_id
