from django.contrib import admin
from .models import Service

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description' ,'price', 'date_created')

admin.site.register(Service, ServiceAdmin)


