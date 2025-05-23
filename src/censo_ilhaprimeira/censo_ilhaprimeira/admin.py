from django.contrib import admin
from .models import Morador, Domicilio, Falecido

admin.site.register(Morador)
admin.site.register(Domicilio)
admin.site.register(Falecido)