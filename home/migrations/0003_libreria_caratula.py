# Generated by Django 4.1.1 on 2022-12-14 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_libreria_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='libreria',
            name='caratula',
            field=models.ImageField(blank=True, null=True, upload_to='caratulas'),
        ),
    ]
