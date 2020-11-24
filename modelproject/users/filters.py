import django_filters
from .models import *

class filterProduct(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = ['name','price','category']
