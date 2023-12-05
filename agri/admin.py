from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Crop)
admin.site.register(CropTask)
admin.site.register(UOM)
admin.site.register(CropLocation)
admin.site.register(CropCycle)
admin.site.register(PlantAnalysis)
admin.site.register(PlantAnalysisCriteria)
admin.site.register(Location)
admin.site.register(SoilAnalysis)
admin.site.register(SoilAnalysisCriteria)
admin.site.register(SoilType)
admin.site.register(SoilTexture)
admin.site.register(SoilTextureCriteria)
admin.site.register(Weather)
