from django import forms
from .models import *
from django.contrib.auth.models import User

class DevicesForm(forms.ModelForm):
    class Meta:
        model = Devices

        fields = ["name", "ip_addr", "serial_num", "mac_addr", "port", "wx_btn", "zero_btn", "tara_btn", "man_tara_btn", "x10_btn","certi_num","max_weight","min_weight","e_d"]
        labels = {
            'name': "Name",
            'ip_addr': "IP Address",
            'serial_num': "Serial Number",
            'mac_addr': "MAC ",
            'port': "Port",
            'wx_btn': "Enable WX Button",
            'zero_btn': "Enable Zero Button",
            'tara_btn': "Enable Tara Button",
            'man_tara_btn': "Enable Man Tara Button",
            'x10_btn': "Enable x10 Button",
            'max_weight': "Max Weight",
            'min_weight': "Min Weight",
            'e_d': "E/D",
            'certi_num': "Certificate Num",
        }


class LoginForm(forms.ModelForm):
    class Meta:
        model = User

        fields = ["username", "password"]
        labels = {
            'password': "Password",
        }


