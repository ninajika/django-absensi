from django.contrib import admin

from HistoriKehadiran.models import HistoriKehadiran

# Register your models here.
class HistoriKehadiranAdmin(admin.ModelAdmin):
    list_display = ["id_mhs", "tanggal", "status"]
    list_filter = ["tanggal", "status"]
    search_fields = ["id_mhs__nama", "tanggal", "status"]
    #raw_id_fields = ("id_mhs",)
    ordering = ["-tanggal"]
    actions = ["make_alpa", "make_izin", "make_sakit", "make_hadir"]

    def make_alpa(self, request, queryset):
        queryset.update(status="Alpa")
    make_alpa.short_description = "Mark selected as Alpa"

    def make_izin(self, request, queryset):
        queryset.update(status="Izin")
    make_izin.short_description = "Mark selected as Izin"

    def make_sakit(self, request, queryset):
        queryset.update(status="Sakit")
    make_sakit.short_description = "Mark selected as Sakit"

    def make_hadir(self, request, queryset):
        queryset.update(status="Hadir")
    make_hadir.short_description = "Mark selected as Hadir"


admin.site.register(HistoriKehadiran, HistoriKehadiranAdmin)
