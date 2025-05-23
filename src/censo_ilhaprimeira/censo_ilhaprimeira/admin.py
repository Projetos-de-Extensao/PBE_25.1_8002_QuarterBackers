from django.contrib import admin
from .models import Morador, Domicilio

admin.site.register(Morador)
admin.site.register(Domicilio)