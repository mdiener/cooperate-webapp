# Generated by Django 4.2.6 on 2023-10-11 00:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[(1, '0011'), (2, '1011'), (3, '1111'), (4, '1010')], max_length=200)),
                ('cost_share', models.DecimalField(decimal_places=2, max_digits=3)),
            ],
        ),
        migrations.RemoveField(
            model_name='ad',
            name='cost_share',
        ),
        migrations.AlterField(
            model_name='ad',
            name='ad_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ads.adtype'),
        ),
    ]
