from django.contrib import admin

# Register your models here.
from .models import Data, Prod

admin.site.register(Data)
admin.site.register(Prod)

