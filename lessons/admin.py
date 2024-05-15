from django.contrib import admin
from .models import *
@admin.register(Subject)
class AdminSubject(admin.ModelAdmin):
    list_display = ['subject_name']


@admin.register(SubjectGroupSchedule)
class AdminSGS(admin.ModelAdmin):
    search_fields = ["day_of_week","date_of_week"]
