# Generated by Django 4.0.5 on 2022-06-19 19:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('comTwitter', '0002_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='updated_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]