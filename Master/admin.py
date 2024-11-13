from django.contrib import admin

# Register your models here.
from django.db.models import F


# Import the necessary models

from .models import Dosen, Mahasiswa, MataKuliah
from unfold.admin import ModelAdmin

@admin.register(Dosen)
class DosenAdmin(ModelAdmin):
    list_display = ["id", "nama", "email", "prodi"]
    ordering = ["nama"]
    search_fields = ["nama", "email", "prodi"]
    actions = ["assign_prodiTI", "assign_prodiTS", "assign_prodiBTP"]

    def assign_prodiTI(self, request, queryset):
        queryset.update(prodi="Teknologi Informasi")
    assign_prodiTI.short_description = "Assign default Prodi (Teknologi Informasi)"

    def assign_prodiTS(self, request, queryset):
        queryset.update(prodi="Teknik Sipil")
    assign_prodiTS.short_description = "Assign default Prodi (Teknik Sipil)"

    def assign_prodiBTP(self, request, queryset):
        queryset.update(prodi="Teknik Bisnis dan Tanaman Perkebunan")
    assign_prodiBTP.short_description = "Assign Prodi (Teknik Bisnis dan Tanaman Perkebunan)"



@admin.register(MataKuliah)
class MataKuliahAdmin(ModelAdmin):
    list_display = ["nama_matakuliah", "sks", "dosen_pengampu"]
    list_filter = ["sks"]
    search_fields = ["nama_matakuliah", "sks", "dosen_pengampu"]
    ordering = ["nama_matakuliah"]
    actions = ["make_sks_2", "make_sks_3", "make_sks_4"]

    def make_sks_2(self, request, queryset):
        queryset.update(sks=2)
    make_sks_2.short_description = "Set SKS to 2"

    def make_sks_3(self, request, queryset):
        queryset.update(sks=3)
    make_sks_3.short_description = "Set SKS to 3"

    def make_sks_4(self, request, queryset):
        queryset.update(sks=4)
    make_sks_4.short_description = "Set SKS to 4"

@admin.register(Mahasiswa)
class MahasiswaAdmin(ModelAdmin):
    list_display = ["email", "nomor_telepon", "nim", "jenis_kelamin", "prodi", "terlambat", "tidak_hadir", "semester"]  # Ensure these fields exist in the model
    list_filter = ["prodi", "semester"]
    search_fields = ["email", "nomor_telepon", "nim", "prodi", "terlambat", "tidak_hadir", "semester"]
    ordering = ["email"] 
    actions = ["increase_terlambat", "decrease_terlambat", "increase_tidak_hadir", "decrease_tidak_hadir", "increase_semester", "decrease_semester", "make_laki_laki", "make_perempuan"]

    def increase_terlambat(self, request, queryset):
        queryset.update(terlambat=F("terlambat") + 1)
    increase_terlambat.short_description = "Menambah Terlambat sebanyak 1"
    
    def decrease_terlambat(self, request, queryset):
        queryset.update(terlambat=F("terlambat") - 1)
    decrease_terlambat.short_description = "Mengurangi Terlambat sebanyak 1"
    
    def increase_tidak_hadir(self, request, queryset):
        queryset.update(tidak_hadir=F("tidak_hadir") + 1)
    increase_tidak_hadir.short_description = "Menambah Tidak Hadir sebanyak 1"
    
    def decrease_tidak_hadir(self, request, queryset):
        queryset.update(tidak_hadir=F("tidak_hadir") - 1)
    decrease_tidak_hadir.short_description = "Mengurangi Tidak Hadir sebanyak 1"
    
    def increase_semester(self, request, queryset):
        queryset.update(semester=F("semester") + 1)
    increase_semester.short_description = "Menambah Semester sebanyak 1"
    
    def decrease_semester(self, request, queryset):
        queryset.update(semester=F("semester") - 1)
    decrease_semester.short_description = "Mengurangi Semester sebanyak 1"
    
    def make_laki_laki(self, request, queryset):
        queryset.update(jenis_kelamin="Laki-laki")
    make_laki_laki.short_description = "Menandai sebagai Laki-laki"
    
    def make_perempuan(self, request, queryset):
        queryset.update(jenis_kelamin="Perempuan")
    make_perempuan.short_description = "Menandai sebagai Perempuan"



# Register models with the admin
# admin.site.register(Dosen, DosenAdmin)
# admin.site.register(Mahasiswa, MahasiswaAdmin)
# admin.site.register(MataKuliah, MataKuliahAdmin)
