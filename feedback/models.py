from django.db import models

# Create your models here.
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Feedback(models.Model):
    # Bikin Generic foreign key untuk pengirim
    pengirim_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, related_name='feedback_pengirim')
    pengirim_object_id = models.PositiveIntegerField()
    id_pengirim = GenericForeignKey('pengirim_content_type', 'pengirim_object_id')
    
    # Bikin Generic foreign key untuk penerima
    penerima_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, related_name='feedback_penerima')
    penerima_object_id = models.PositiveIntegerField()
    id_penerima = GenericForeignKey('penerima_content_type', 'penerima_object_id')
    
    isi_feedback = models.TextField(null=True)
    tanggal = models.DateField(null=True)
