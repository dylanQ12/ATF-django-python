from django.contrib import admin
from .models import Carrusel


class CarruselAdmin(admin.ModelAdmin):
    list_display = ["title", "date_created"]


admin.site.register(Carrusel, CarruselAdmin)
