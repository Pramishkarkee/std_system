# Generated by Django 2.2.11 on 2020-04-02 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0009_auto_20200402_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='noSem',
            field=models.IntegerField(default='', max_length=30),
        ),
    ]
