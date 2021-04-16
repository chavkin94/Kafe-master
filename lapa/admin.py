from django.contrib import admin

# Register your models here.
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin, ImportExportModelAdmin

from lapa.models import TipTovara, Tovar, Akzia, Zakaz, Otzivi

admin.site.register(TipTovara)

admin.site.register(Tovar)

admin.site.register(Akzia)

admin.site.register(Zakaz)

admin.site.register(Otzivi)
