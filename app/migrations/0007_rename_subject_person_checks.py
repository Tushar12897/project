# Generated by Django 4.1.1 on 2023-10-22 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_person_subject'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='subject',
            new_name='checks',
        ),
    ]
