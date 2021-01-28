from django.urls import include, path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'divisions', views.DivisionViewSet)
router.register(r'districts', views.DistrictViewSet)
router.register(r'upazilas', views.UpazilaViewSet)

app_name = 'general'
urlpatterns = [
    path('api/', include(router.urls))
]