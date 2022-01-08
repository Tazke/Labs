# Generated by Django 3.2 on 2022-01-06 13:36

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume_module', models.CharField(default='', max_length=50)),
                ('name_module', models.CharField(default='', max_length=50)),
                ('start_module', models.TimeField(null=True)),
                ('finish_module', models.TimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RoomPetition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_petition', models.CharField(default='', max_length=30)),
                ('name_petition', models.CharField(default='', max_length=50)),
                ('email_petition', models.CharField(default='', max_length=50)),
                ('computer_petition', models.IntegerField(default='')),
                ('date_start_petition', models.DateField(null=True)),
                ('date_finish_petition', models.DateField(null=True)),
                ('day_petition', models.CharField(choices=[('1', 'Lunes'), ('2', 'Martes'), ('3', 'Miercoles'), ('4', 'Jueves'), ('5', 'Viernes'), ('6', 'Sabado'), ('0', 'Domingo')], default='1', max_length=1, null=True)),
                ('time_start_petition', models.TimeField(null=True)),
                ('time_finish_petition', models.TimeField(null=True)),
                ('recurrence_petition', models.CharField(choices=[('01', 'Diario'), ('07', 'Semanal'), ('28', 'Mensual')], default='01', max_length=2)),
                ('memo_petition', models.CharField(default='', max_length=100, null=True)),
                ('type_petition', models.CharField(choices=[('N', 'Normal'), ('E', 'Extraordinario')], default='N', max_length=1)),
                ('status_petition', models.CharField(choices=[('P', 'Pendiente'), ('A', 'Aceptada'), ('R', 'Rechazada')], default='P', max_length=1, null=True)),
                ('datetime_petition', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
                ('room_petition', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.room')),
            ],
        ),
        migrations.CreateModel(
            name='ModuleEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField()),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedules.module')),
                ('petition', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='schedules.roompetition')),
            ],
        ),
    ]
