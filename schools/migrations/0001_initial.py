# Generated by Django 3.1.5 on 2021-02-23 10:01

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='School Name')),
                ('province', models.CharField(choices=[('Northern Province', 'Northern Province'), ('Eastern Province', 'Eastern Province'), ('Western Province', 'Western Province'), ('Southern Province', 'Southern Province'), ('Kigali City', 'Kigali City')], max_length=30, verbose_name='School Province')),
                ('district', models.CharField(max_length=50, verbose_name='School District')),
                ('level', models.CharField(choices=[('Pre-Nursery', 'Pre-Nursery'), ('Nursery', 'Nursery'), ('Primary', 'Primary'), ('General Secondary', 'General Secondary'), ('TVET', 'TVET'), ('General Tertiary', 'General Tertiary'), ('Adult Literacy', 'Adult Literacy')], max_length=30, verbose_name='School Level')),
                ('male', models.IntegerField(default=0, verbose_name='Male Students')),
                ('female', models.IntegerField(default=0, verbose_name='Female Students')),
                ('electricity_availability', models.BooleanField(default=False, verbose_name='Electricity Availability')),
                ('school_code', models.IntegerField(default=0, verbose_name='School Code')),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326, verbose_name='School location')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('updated_at', models.DateTimeField(verbose_name='Date Updated')),
            ],
        ),
    ]
