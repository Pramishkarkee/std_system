# Generated by Django 2.2.11 on 2020-04-03 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0011_auto_20200402_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='noSem',
            field=models.CharField(default='', max_length=30),
        ),
    ]
