# Generated by Django 4.2.6 on 2023-10-11 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0004_alter_adtype_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='date',
            field=models.DateField(verbose_name='date published'),
        ),
    ]
