from django.contrib import admin
from .models import Pages


class PagesAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name = u'Something'
        verbose_name_plural = u'Something'


admin.site.register(Pages, PagesAdmin)

