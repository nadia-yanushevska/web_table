from django.contrib import admin
from .models import DataSchema, Table

# Register your models here.
admin.site.register(Table)
admin.site.register(DataSchema)