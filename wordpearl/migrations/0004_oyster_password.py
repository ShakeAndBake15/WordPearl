# Generated by Django 4.1.3 on 2022-11-15 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wordpearl', '0003_comment_body_pearl_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='oyster',
            name='password',
            field=models.CharField(default=' ', max_length=50),
            preserve_default=False,
        ),
    ]
