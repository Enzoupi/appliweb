from django.contrib import admin

# Register your models here.
from .models import Data, Prod, Recipe

admin.site.register(Data)
admin.site.register(Prod)
admin.site.register(Recipe)

