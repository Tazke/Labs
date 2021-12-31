# Generated by Django 3.2 on 2021-12-31 00:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Externuser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=60, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='TicketReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=200)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('state', models.CharField(blank=True, choices=[('A', 'Abierto'), ('C', 'Cerrado')], default='A', max_length=1, null=True)),
                ('comment', models.CharField(blank=True, max_length=200, null=True)),
                ('date_comment', models.DateTimeField(blank=True, null=True)),
                ('email', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='monitoring.externuser')),
                ('pc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.workstation')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='ScheduledReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_scheduled', models.DateTimeField()),
                ('title', models.CharField(max_length=50)),
                ('room', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.room')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Revision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monitor', models.CharField(choices=[('P', 'Presenta'), ('NP', 'No Presenta'), ('D', 'Dañado')], default='', max_length=2)),
                ('mouse', models.CharField(choices=[('P', 'Presenta'), ('NP', 'No Presenta'), ('D', 'Dañado')], default='', max_length=2)),
                ('keyboard', models.CharField(choices=[('P', 'Presenta'), ('NP', 'No Presenta'), ('D', 'Dañado')], default='', max_length=2)),
                ('cpu', models.CharField(choices=[('P', 'Presenta'), ('NP', 'No Presenta'), ('D', 'Dañado')], default='', max_length=2)),
                ('SO', models.CharField(choices=[('O', 'Operativo'), ('F', 'Falla'), ('N', 'No Tiene')], default='', max_length=2)),
                ('software', models.CharField(choices=[('O', 'Operativo'), ('F', 'Falla'), ('N', 'No Tiene')], default='', max_length=2)),
                ('observation', models.CharField(max_length=200)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('pc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.workstation')),
                ('scheduled_review', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='monitoring.scheduledreview')),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
