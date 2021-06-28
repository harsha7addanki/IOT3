from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
	filter_horizontal = ('things','devices')


@admin.register(Thing)
class ThingAdmin(admin.ModelAdmin):
	filter_horizontal = ('properties',)


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
	pass


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
	pass


AS = admin.site
AS.site_header = "Developer Interface"
AS.site_title = "Developer Interface"
