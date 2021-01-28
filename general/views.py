from django.shortcuts import render

from .models import Division, District, Upazila
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import DivisionSerializer, DistrictSerializer, UpazilaSerializer
# Create your views here.


class DivisionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows division to be viewed or edited.
    """
    queryset = Division.objects.all()
    serializer_class = DivisionSerializer
    http_method_names = ['get']
    # permission_classes = [permissions.IsAuthenticated]


class DistrictViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows district to be viewed or edited.
    """
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    http_method_names = ['get']


class UpazilaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows district to be viewed or edited.
    """
    queryset = Upazila.objects.all()
    serializer_class = UpazilaSerializer
    http_method_names = ['get']