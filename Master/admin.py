from django.contrib import admin

# Register your models here.
from django.db.models import F

from HistoriKehadiran.models import HistoriKehadiran
from KRS.models import KRS
from UserProfile.models import UserProfile
from feedback.models import Feedback

# Import the necessary models

from .models import Dosen, Mahasiswa, MataKuliah

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "is_dosen"]
    list_filter = ["is_dosen"]
    search_fields = ["user__username", "is_dosen"]
    actions = ["make_dosen", "remove_dosen"]

    def make_dosen(self, request, queryset):
        queryset.update(is_dosen=True)
    make_dosen.short_description = "Set selected users as Dosen"

    def remove_dosen(self, request, queryset):
        queryset.update(is_dosen=False)
    remove_dosen.short_description = "Remove Dosen status from selected users"

class DosenAdmin(admin.ModelAdmin):
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

class MataKuliahAdmin(admin.ModelAdmin):
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

class MahasiswaAdmin(admin.ModelAdmin):
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
    
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ["isi_feedback", "tanggal"]
    list_filter = ["tanggal"]
    search_fields = ["isi_feedback", "tanggal"]

class KRSAdmin(admin.ModelAdmin):
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

# Register models with the admin
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Dosen, DosenAdmin)
admin.site.register(HistoriKehadiran, HistoriKehadiranAdmin)
admin.site.register(Mahasiswa, MahasiswaAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(KRS, KRSAdmin)
admin.site.register(MataKuliah, MataKuliahAdmin)
