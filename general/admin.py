from django.contrib import admin


from .models import Division
from .models import District
from .models import Upazila
# Register your models here.

class DistrictInline(admin.StackedInline):
	model = District
	can_delete = Falseverbose_name_plural = 'Districts'

class UpazilaInline(admin.StackedInline):
	model = Upazila
	can_delete = Falseverbose_name_plural = 'Upazilas'

class DivisionAdmin(admin.ModelAdmin):
    inlines = (DistrictInline, UpazilaInline)




admin.site.register(Division)
admin.site.register(District)
admin.site.register(Upazila)