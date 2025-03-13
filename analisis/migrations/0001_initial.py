# Generated by Django 3.2.6 on 2025-03-13 04:05

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('examen_eeg', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Analisis',
            fields=[
                ('examen_eeg', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='examen_eeg.exameneeg')),
                ('descripcion', models.CharField(max_length=1000)),
                ('deteccion_anomalias', models.CharField(default=None, max_length=1000)),
                ('fecha_analisis', models.DateField(default=datetime.date.today)),
            ],
        ),
    ]
