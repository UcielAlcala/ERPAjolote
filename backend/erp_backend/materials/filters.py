# erp_backend/materials/filters.py

from django_filters import rest_framework as filters
from .models import Material
from django.db.models import Q

class MaterialFilter(filters.FilterSet):
    type = filters.CharFilter(field_name='type', lookup_expr='exact')
    sub_type = filters.BaseInFilter(field_name='sub_type', lookup_expr='in')
    custom_filter = filters.CharFilter(method='filter_by_type_or_sub_type')

    class Meta:
        model = Material
        fields = ['type', 'sub_type', 'custom_filter']

    def filter_by_type_or_sub_type(self, queryset, name, value):
        sub_types = value.split(',')
        return queryset.filter(
            Q(type='Empaque') | Q(sub_type__in=sub_types)
        )
