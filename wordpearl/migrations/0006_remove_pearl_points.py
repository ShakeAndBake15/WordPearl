# Generated by Django 4.1.3 on 2022-11-15 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wordpearl', '0005_pearl_points'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pearl',
            name='points',
        ),
    ]