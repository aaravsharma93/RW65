from django import forms
from . import models


class LocationForm(forms.ModelForm):
    class Meta:
        model = models.Location
        fields = ('name', 'long_lat', 'area')


class UOMForm(forms.ModelForm):
    class Meta:
        model = models.UOM
        fields = ('name',)


class CropCycleForm(forms.ModelForm):
    class Meta:
        model = models.CropCycle
        fields = ('title', 'crop', 'locations', 'start_date',
                  'crop_spacing', 'row_spacing', 'crop_spacing_uom',
                  'row_spacing_uom', 'iso_8601', 'cycle_type')


