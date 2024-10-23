from django.db import models

from Master.models import Mahasiswa

# Create your models here.
class HistoriKehadiran(models.Model):
    proxy = True
    id_mhs = models.ForeignKey(Mahasiswa, on_delete=models.CASCADE)
    tanggal = models.DateField(null=True)
    status = models.CharField(max_length=20, null=True, choices=[('Hadir', 'Hadir'), ('Alpa', 'Alpa'), ('Izin', 'Izin'), ('Sakit', 'Sakit')])

    # def __str__(self):
    #     return str(self.id_mhs.nim)