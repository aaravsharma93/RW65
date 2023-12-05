from django.db.models import JSONField
from django.db import models


# Create your models here.
class Crop(models.Model):
    title = models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=100, null=True)
    scientific_name = models.CharField(max_length=100, null=True, blank=True)
    # task = models.ForeignKey(CropTask, on_delete=models.CASCADE, null=True, blank=True)
    crop_spacing = models.FloatField(blank=True, null=True)
    row_spacing = models.FloatField(blank=True, null=True)
    crop_spacing_uom = models.CharField(max_length=50, null=True, blank=True)
    row_spacing_uom = models.CharField(max_length=50, null=True, blank=True)
    type = models.CharField(max_length=50, null=True, blank=True)
    category = models.CharField(max_length=100, null=True, blank=True)
    target_warehouse = models.ForeignKey(
        "yard.Warehouse", on_delete=models.CASCADE, null=True, blank=True)
    planting_uom = models.CharField(max_length=50, null=True, blank=True)
    yield_uom = models.CharField(max_length=50, null=True, blank=True)
    planting_area = models.CharField(max_length=50, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title


class CropTask(models.Model):
    name = models.CharField(max_length=100, null=True)
    start_day = models.CharField(max_length=100, null=True)
    end_day = models.CharField(max_length=100, null=True)
    holiday_management = models.CharField(max_length=100, null=True)
    priority = models.CharField(max_length=100, null=True)
    crop_id = models.ForeignKey(
        Crop, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class CropCycle(models.Model):
    Cycle_TIME = (
        ('YR', 'YEARLY'),
        ('LYR', 'LESS THAN A YEAR')
    )
    title = models.CharField(max_length=1000, unique=True, null=True)
    crop = models.ForeignKey(
        Crop, on_delete=models.CASCADE, null=True, blank=True)
    locations = models.ManyToManyField("agri.Location", blank=True)
    start_date = models.CharField(max_length=100, null=True, blank=True)
    crop_spacing = models.FloatField(blank=True, null=True)
    row_spacing = models.FloatField(blank=True, null=True)
    crop_spacing_uom = models.CharField(max_length=50, null=True, blank=True)
    row_spacing_uom = models.CharField(max_length=50, null=True, blank=True)
    iso_8601 = models.BooleanField(default=False, null=True)
    cycle_type = models.CharField(
        choices=Cycle_TIME, max_length=100, default='YR')


class UOM(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=1000, null=True)
    long_lat = JSONField(null=True, blank=True)
    area = models.FloatField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.name) if self.name else ''


class CropLocation(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    crop = models.ForeignKey(
        Crop, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.location)


class PlantAnalysis(models.Model):
    name = models.CharField(max_length=1000, null=True, blank=True)
    crop = models.ForeignKey(
        Crop, on_delete=models.CASCADE, null=True, blank=True)
    collection_datetime = models.CharField(
        max_length=100, null=True, blank=True)
    lab_test_datetime = models.CharField(max_length=100, null=True, blank=True)
    result_datetime = models.CharField(max_length=100, null=True, blank=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.name)


class PlantAnalysisCriteria(models.Model):
    title = models.CharField(max_length=1000, null=True, blank=True)
    value = models.CharField(max_length=100, null=True, blank=True)
    max_permissible_value = models.CharField(
        max_length=100, null=True, blank=True)
    min_permissible_value = models.CharField(
        max_length=100, null=True, blank=True)
    plant_analysis = models.ForeignKey(
        PlantAnalysis, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.title)


class SoilAnalysis(models.Model):
    name = models.CharField(max_length=1000, null=True, blank=True)
    invoice_number = models.CharField(max_length=1000, null=True, blank=True)
    collection_datetime = models.CharField(
        max_length=100, null=True, blank=True)
    lab_test_datetime = models.CharField(max_length=100, null=True, blank=True)
    result_datetime = models.CharField(max_length=100, null=True, blank=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class SoilAnalysisCriteria(models.Model):
    title = models.CharField(max_length=1000, null=True, blank=True)
    value = models.CharField(max_length=100, null=True, blank=True)
    max_permissible_value = models.CharField(
        max_length=100, null=True, blank=True)
    min_permissible_value = models.CharField(
        max_length=100, null=True, blank=True)
    soil_analysis = models.ForeignKey(
        SoilAnalysis, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title


class SoilType(models.Model):
    name = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return str(self.name)


class SoilTexture(models.Model):
    name = models.CharField(max_length=1000, null=True, blank=True)
    soil_type = models.ForeignKey(
        SoilType, on_delete=models.CASCADE, null=True)
    clay_composition = models.FloatField(null=True, blank=True)
    sand_composition = models.FloatField(null=True, blank=True)
    silt_composition = models.FloatField(null=True, blank=True)
    collection_datetime = models.CharField(
        max_length=100, null=True, blank=True)
    lab_test_datetime = models.CharField(max_length=100, null=True, blank=True)
    result_datetime = models.CharField(max_length=100, null=True, blank=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.name)


class SoilTextureCriteria(models.Model):
    title = models.CharField(max_length=1000, null=True, blank=True)
    value = models.CharField(max_length=100, null=True, blank=True)
    max_permissible_value = models.CharField(
        max_length=100, null=True, blank=True)
    min_permissible_value = models.CharField(
        max_length=100, null=True, blank=True)
    soil_texture = models.ForeignKey(
        SoilTexture, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title


class Weather(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    day_temp = models.CharField(max_length=50, null=True, blank=True)
    min_temp = models.CharField(max_length=50, null=True, blank=True)
    max_temp = models.CharField(max_length=50, null=True, blank=True)
    night_temp = models.CharField(max_length=50, null=True, blank=True)
    evn_temp = models.CharField(max_length=50, null=True, blank=True)
    morn_temp = models.CharField(max_length=50, null=True, blank=True)
    pressure = models.CharField(max_length=50, null=True, blank=True)
    dew_point = models.CharField(max_length=50, null=True, blank=True)
    humidity = models.CharField(max_length=50, null=True, blank=True)
    description = models.CharField(max_length=50, null=True, blank=True)
    clouds = models.CharField(max_length=50, null=True, blank=True)
    rain = models.CharField(max_length=50, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.location.name)
