# Generated by Django 4.0.5 on 2022-06-21 01:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comTwitter', '0005_business_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='business',
            name='user',
        ),
    ]