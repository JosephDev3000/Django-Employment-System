from django.contrib import admin
from .models import Roles, Hired
from django.contrib.auth.models import Group

admin.site.site_header = 'Database Dashboard'

class RolesAdmin(admin.ModelAdmin):
    list_display = ('name','category','quantity',)
    list_filter = ['category']

# Register your models here.
admin.site.register(Roles, RolesAdmin)
admin.site.register(Hired)
# admin.site.unregister(Group)