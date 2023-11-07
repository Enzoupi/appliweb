import django_filters
from django_filters import rest_framework as filters

from .models import *

class ProdFilter(django_filters.FilterSet):
    class Meta:
         model = Prod
         fields = ['date','boulanger']
         
