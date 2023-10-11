# Generated by Django 4.2.6 on 2023-10-10 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad_type', models.CharField(max_length=200)),
                ('date', models.DateTimeField(verbose_name='date published')),
                ('cost_share', models.DecimalField(decimal_places=2, max_digits=3)),
                ('actual_spend', models.DecimalField(decimal_places=2, max_digits=14)),
            ],
        ),
    ]