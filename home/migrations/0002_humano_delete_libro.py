# Generated by Django 4.1.1 on 2022-10-17 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Libreria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30)),
                ('genero', models.CharField(max_length=30)),
                ('mes_venta', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='Libro',
        ),
    ]