from django.contrib import admin
from .models import Notice,Event,EventForm

from import_export.admin import ImportExportModelAdmin

# Register your models here.

@admin.register(Notice,Event,EventForm)


class ViewAdmin(ImportExportModelAdmin):
    pass

admin.site.site_header = "Mantra 7Hills Administrator"