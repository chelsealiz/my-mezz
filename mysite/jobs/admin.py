__author__ = 'zobair'
from django.contrib import admin
from models import Job


class JobAdmin(admin.ModelAdmin):
    class Meta:
        model = Job

admin.site.register(Job, JobAdmin)
