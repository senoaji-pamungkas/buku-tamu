# Generated by Django 4.0.6 on 2022-08-06 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0006_alter_karyawan_divisi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='karyawan',
            name='divisi',
            field=models.CharField(choices=[(('It',), ('It',)), ('Pemasaran', 'Pemasaran')], max_length=20),
        ),
    ]
