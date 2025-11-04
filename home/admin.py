from django.contrib import admin
from .models import Disfraz

admin.site.register(Disfraz)

class DisfrazAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'imagen')