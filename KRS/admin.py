from django.contrib import admin

from KRS.models import KRS
from unfold.admin import ModelAdmin

# Register your models here.
@admin.register(KRS)
class KRSAdmin(ModelAdmin):
    list_display = ["id_mhs", "id_matkul", "wajib"]
    list_filter = ["wajib"]
    search_fields = ["id_mhs__nama", "id_matkul__nama_matakuliah"]
    #raw_id_fields = ("id_mhs", "id_matkul")
    ordering = ["id_mhs"]
    actions = ["make_wajib", "make_optional"]

    def make_wajib(self, request, queryset):
        queryset.update(wajib="Ya")
    make_wajib.short_description = "Set as Wajib (Ya)"

    def make_optional(self, request, queryset):
        queryset.update(wajib="Tidak")
    make_optional.short_description = "Set as Optional (Tidak)"

# admin.site.register(KRS, KRSAdmin)
