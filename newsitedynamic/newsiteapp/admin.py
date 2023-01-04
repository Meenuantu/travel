from django.contrib import admin

# Register your models here.
from .models import place,teams
admin.site.register(place)
admin.site.register(teams)