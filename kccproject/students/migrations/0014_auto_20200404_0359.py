# Generated by Django 2.2.11 on 2020-04-04 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0013_studentdetail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdetail',
            name='studentPicture',
            field=models.FileField(upload_to='uploadfile/'),
        ),
    ]
