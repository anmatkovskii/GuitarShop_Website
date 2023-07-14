from django_filters import rest_framework as filters
from .models import Guitar, GuitarImage


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class IntFilterInFilter(filters.BaseInFilter, filters.NumberFilter):
    pass


class GuitarFilter(filters.FilterSet):
    type = CharFilterInFilter(field_name='type', lookup_expr='in')
    prod_name = CharFilterInFilter(field_name='prod_name', lookup_expr='in')
    body = CharFilterInFilter(field_name='body', lookup_expr='in')
    body_material = CharFilterInFilter(field_name='body_material', lookup_expr='in')
    neck_attachment = CharFilterInFilter(field_name='neck_attachment', lookup_expr='in')
    scale = CharFilterInFilter(field_name='scale', lookup_expr='in')
    bridge = CharFilterInFilter(field_name='bridge', lookup_expr='in')
    frets = CharFilterInFilter(field_name='frets', lookup_expr='in')
    fretboard_material = CharFilterInFilter(field_name='fretboard_material', lookup_expr='in')
    fretboard_pad_material = CharFilterInFilter(field_name='fretboard_pad_material', lookup_expr='in')

    strings = IntFilterInFilter(field_name='strings', lookup_expr='in')

    prod_price = filters.RangeFilter(field_name='prod_price')

    class Meta:
        model = Guitar
        fields = ['type', 'prod_name', 'prod_price', 'body', 'strings', 'body_material', 'neck_attachment',
                  'scale', 'bridge', 'frets', 'fretboard_material', 'fretboard_pad_material']
