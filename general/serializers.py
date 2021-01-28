from .models import Division, District, Upazila
from rest_framework import serializers


class DivisionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Division
        fields = ['name', 'bn_name']


class DistrictSerializer(serializers.HyperlinkedModelSerializer):
	# user = serializers.ReadOnlyField(source = 'user.username')
    division = DivisionSerializer()
    class Meta:
        model = District
        fields = ['name', 'bn_name', 'website', 'division']

class UpazilaSerializer(serializers.HyperlinkedModelSerializer):
	district = DistrictSerializer()
	class Meta:
		model = Upazila
		fields = ['name', 'bn_name', 'district']