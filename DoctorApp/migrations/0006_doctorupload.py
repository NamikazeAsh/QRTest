# Generated by Django 4.0.1 on 2023-07-20 09:16

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DoctorApp', '0005_doctormodel_specialization'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('contact', models.CharField(max_length=100)),
                ('pdfs', models.FileField(null=True, upload_to='pdfs', validators=[django.core.validators.FileExtensionValidator(['pdf', ''])])),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DoctorApp.doctormodel')),
            ],
        ),
    ]
