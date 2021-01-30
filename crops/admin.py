from django.contrib import admin
from .models import Crop, CropSeason, CropVariety, CropStage

# Register your models here.



admin.site.register(Crop)
admin.site.register(CropSeason)
admin.site.register(CropVariety)
admin.site.register(CropStage)
