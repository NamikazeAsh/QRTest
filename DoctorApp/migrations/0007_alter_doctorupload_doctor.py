# Generated by Django 4.0.1 on 2023-07-20 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DoctorApp', '0006_doctorupload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorupload',
            name='doctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='DoctorApp.doctormodel'),
        ),
    ]
