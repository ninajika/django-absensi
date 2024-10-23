from django.db import models

from Master.models import Mahasiswa, MataKuliah

# Create your models here.
class KRS(models.Model):
    id_mhs = models.ForeignKey(Mahasiswa, on_delete=models.CASCADE)
    id_matkul = models.ForeignKey(MataKuliah, on_delete=models.CASCADE)
    wajib = models.CharField(max_length=5, choices=[('Ya', 'Ya'), ('Tidak', 'Tidak')], null=True)
