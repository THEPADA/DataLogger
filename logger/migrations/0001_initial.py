# Generated by Django 2.0.2 on 2018-02-20 17:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WaterLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance', models.CharField(max_length=400)),
                ('rTCtemp', models.CharField(max_length=400)),
                ('watertemp', models.CharField(max_length=400)),
                ('airttemp', models.CharField(max_length=400)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]