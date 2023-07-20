# Generated by Django 4.0.1 on 2023-07-20 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DoctorApp', '0004_doctormodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctormodel',
            name='specialization',
            field=models.CharField(choices=[('Orthopedic', 'Orthopedic'), ('Piles', 'Piles'), ('Fissures', 'Fissures'), ('Cataract', 'Cataract')], default='-', max_length=100),
        ),
    ]
