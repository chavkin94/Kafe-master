from django.contrib import admin

# Register your models here.
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin, ImportExportModelAdmin

from lapa.models import TipTovara, Tovar, Akzia, Zakaz, Otzivi

# class TipTovaraAdmin(ImportExportModelAdmin):
#     pass
#
# admin.site.register(TipTovara)
#
#
# admin.site.register(Tovar)
class TipTovaraAdmin(admin.ModelAdmin):
    pass

admin.site.register(TipTovara, TipTovaraAdmin)


class TovarAdmin(ImportExportActionModelAdmin):
    list_display = [
        'id',
        'nazvanie',
        'opisanie',
        'cena',
        'prevyu',
        'tip_tovara',
        'kolvo_dobavlenia_v_korzinu'
    ]
    list_filter = ('tip_tovara',)
    readonly_fields = ['kolvo_dobavlenia_v_korzinu', ]
    list_display_links = ['nazvanie', ]
    search_fields = ['nazvanie', 'cena', 'tip_tovara__nazvanie']
    list_editable = ['opisanie', 'cena', 'tip_tovara']
    ordering = ['-nazvanie', ]

admin.site.register(Tovar, TovarAdmin)


class AkziaAdmin(ImportExportModelAdmin):
    list_display = [
        'id',
        'nazvanie',
    ]
    # list_filter = ('nazvanie',)
    list_display_links = ['id', ]
    search_fields = ['nazvanie', ]
    list_editable = ['nazvanie', ]
    ordering = ['-nazvanie', ]

admin.site.register(Akzia, AkziaAdmin)

class ZakazAdmin(admin.ModelAdmin):
    pass


admin.site.register(Zakaz, ZakazAdmin)

class OtziviAdmin(admin.ModelAdmin):
    pass


admin.site.register(Otzivi, OtziviAdmin)
#
# admin.site.register(Zakaz)
#
# admin.site.register(Otzivi)
