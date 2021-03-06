# Generated by Django 3.2 on 2022-01-02 23:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ecguser',
            name='created_at',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ecguser',
            name='experience',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ecguser',
            name='info',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ecguser',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='ecguser',
            name='login',
            field=models.CharField(default=django.utils.timezone.now, max_length=50, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ecguser',
            name='position',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ecguser',
            name='workplace',
            field=models.CharField(default=datetime.datetime(2022, 1, 2, 23, 48, 29, 427983, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ecguser',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='ecguser',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='ecguser',
            name='last_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='ecguser',
            name='password',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
