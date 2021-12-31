# Generated by Django 3.2 on 2021-12-31 00:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('location_latitude', models.CharField(blank=True, max_length=50, null=True)),
                ('location_longitude', models.CharField(blank=True, max_length=50, null=True)),
                ('active', models.BooleanField(default=True)),
                ('inactive_by', models.TextField(blank=True, default='', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_name', models.CharField(blank=True, max_length=50, null=True)),
                ('address', models.CharField(blank=True, max_length=250, null=True)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('inactive_by', models.TextField(default='')),
                ('campus', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.campus')),
            ],
        ),
        migrations.CreateModel(
            name='Workstation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('ip', models.CharField(blank=True, max_length=50, null=True)),
                ('pc_model', models.CharField(blank=True, max_length=50, null=True)),
                ('pc_serialnumber', models.CharField(blank=True, max_length=50, null=True)),
                ('processor_model', models.CharField(blank=True, max_length=50, null=True)),
                ('ram_capacity', models.CharField(blank=True, max_length=50, null=True)),
                ('disk_type', models.CharField(blank=True, max_length=50, null=True)),
                ('disk_capacity', models.CharField(blank=True, max_length=50, null=True)),
                ('monitor_model', models.CharField(blank=True, max_length=50, null=True)),
                ('monitor_serialnumber', models.CharField(blank=True, max_length=15, null=True)),
                ('monitor_inches', models.PositiveIntegerField(default=0)),
                ('active', models.BooleanField(default=True)),
                ('inactive_by', models.TextField(default='')),
                ('room', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.room')),
            ],
        ),
    ]
