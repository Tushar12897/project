# Generated by Django 4.1.1 on 2023-10-22 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_alter_person_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='subject',
            field=models.CharField(max_length=40),
        ),
    ]
