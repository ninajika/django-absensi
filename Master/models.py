from django.db import models

# Create your models here.
class Mahasiswa(models.Model):
    email = models.EmailField(max_length=254, null=True)
    nomor_telepon = models.CharField(max_length=15, null=True)
    nim = models.CharField(max_length=20, null=True, unique=True)
    jenis_kelamin = models.CharField(max_length=10, null=True)
    prodi = models.CharField(max_length=100, null=True)
    terlambat = models.IntegerField(default=0)
    tidak_hadir = models.IntegerField(default=0)
    semester = models.IntegerField(null=True)

    
    def __str__(self):
        return str(self.email)

class MataKuliah(models.Model):
    nama_matakuliah = models.CharField(max_length=100)
    sks = models.IntegerField()
    dosen_pengampu = models.ForeignKey('Dosen', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.nama_matakuliah)
    
class Dosen(models.Model):
    nama = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=254, null=True)
    prodi = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.nama)