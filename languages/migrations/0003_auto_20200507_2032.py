# Generated by Django 3.0.5 on 2020-05-07 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('languages', '0002_auto_20200507_2008'),
    ]

    operations = [
        migrations.RenameField(
            model_name='programmer',
            old_name='languages',
            new_name='lang',
        ),
    ]
