from django.contrib import admin

from .models import *

@admin.register(School)
class AdminSchool(admin.ModelAdmin):
    list_display = ['school_name']


@admin.register(Groups)
class AdminGroups(admin.ModelAdmin):
    list_display = ['group_number','group_teacher']

@admin.register(Pupils)
class AdminPupils(admin.ModelAdmin):
    list_display = ['pupil_fullname','pupil_group']


