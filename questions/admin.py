from django.contrib import admin
from .models import LandType, SoilType, ProblemTopic, Problem
# Register your models here.

admin.site.register(ProblemTopic)
admin.site.register(Problem)
admin.site.register(LandType)
admin.site.register(SoilType)

