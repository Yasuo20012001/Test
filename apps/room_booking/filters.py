import django_filters
from .models import Room


class RoomFilter(django_filters.FilterSet):
    check_in_date = django_filters.DateFilter(field_name='reservation__check_in', lookup_expr='gte')
    check_out_date = django_filters.DateFilter(field_name='reservation__check_out', lookup_expr='lte')
    min_capacity = django_filters.NumberFilter(field_name='capacity', lookup_expr='gte')
    max_capacity = django_filters.NumberFilter(field_name='capacity', lookup_expr='lte')
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Room
        fields = ['check_in_date', 'check_out_date', 'min_capacity', 'max_capacity', 'min_price', 'max_price']
