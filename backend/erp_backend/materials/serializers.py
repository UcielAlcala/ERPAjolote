# erp_backend/materials/serializers.py

from rest_framework import serializers
from .models import Material

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'

    def validate(self, data):
        unit = data.get('unit')
        cost_per_unit = data.get('cost_per_unit')

        if unit == 'kg':
            data['cost_per_unit'] = cost_per_unit / 1000

        return data
