# Generated by Django 4.0.1 on 2023-07-20 09:54

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DoctorApp', '0008_alter_doctorupload_doctor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorupload',
            name='doctor',
            field=models.ForeignKey(blank=True, default='--', null=True, on_delete=django.db.models.deletion.CASCADE, to='DoctorApp.doctormodel'),
        ),
        migrations.AlterField(
            model_name='doctorupload',
            name='pdfs',
            field=models.FileField(null=True, upload_to='pdfs/', validators=[django.core.validators.FileExtensionValidator(['pdf', ''])]),
        ),
    ]
