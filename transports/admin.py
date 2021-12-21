from django.contrib import admin
from .models import Station, Vehicule, Line, Route
# Register your models here.

admin.site.register(Station)
admin.site.register(Line)
admin.site.register(Vehicule)
admin.site.register(Route)