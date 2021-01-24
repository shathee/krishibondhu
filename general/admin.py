from django.contrib import admin


from .models import Division
from .models import District
from .models import Upazila
# Register your models here.


admin.site.register(Division)
admin.site.register(District)
admin.site.register(Upazila)