# Generated by Django 2.0.7 on 2018-07-27 20:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='issue',
            old_name='name',
            new_name='url',
        ),
    ]