from django.contrib import admin
from .models import Peliculas, Promociones, Sala, Schedule

# Register your models here.
admin.site.register(Peliculas)

admin.site.register(Sala)

admin.site.register(Promociones)

admin.site.register(Schedule)