from django.contrib import admin
from .models import servicios

class servicioAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

# Register your models here.

admin.site.register(servicios, servicioAdmin)