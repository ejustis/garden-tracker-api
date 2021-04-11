from rest_framework import serializers
from api.models import SunExposure

class SunExposureSerializer(serializers.ModelSerializer):
    class Meta:
        model = SunExposure
        fields = ('timestamp',
                'garden_id',
                'lux_value')