# Generated by Django 5.1.2 on 2024-11-14 03:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_role_usuarioroles'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Logbook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bitacora', models.TextField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('datacenter', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.datacenter')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
