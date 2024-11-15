# Generated by Django 5.1.1 on 2024-10-15 08:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dosen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100, null=True)),
                ('email', models.CharField(max_length=254, null=True)),
                ('prodi', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mahasiswa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, null=True)),
                ('nomor_telepon', models.CharField(max_length=15, null=True)),
                ('nim', models.CharField(max_length=20, null=True, unique=True)),
                ('jenis_kelamin', models.CharField(max_length=10, null=True)),
                ('prodi', models.CharField(max_length=100, null=True)),
                ('terlambat', models.IntegerField(default=0)),
                ('tidak_hadir', models.IntegerField(default=0)),
                ('semester', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MataKuliah',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_matakuliah', models.CharField(max_length=100)),
                ('sks', models.IntegerField()),
                ('dosen_pengampu', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Master.dosen')),
            ],
        ),
    ]
