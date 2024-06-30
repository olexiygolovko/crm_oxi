import django_filters
from .models import Record

class RecordFilter(django_filters.FilterSet):
    class Meta:
        model = Record
        fields = ['company_name', 'created_at', 'phone', 'city', 'state', 'first_name', 'last_name', 'email']