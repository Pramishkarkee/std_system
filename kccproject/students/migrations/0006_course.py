# Generated by Django 2.2.11 on 2020-04-02 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_auto_20200402_0338'),
    ]

    operations = [
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseCode', models.CharField(default='', max_length=30)),
                ('courseName', models.CharField(default='', max_length=30)),
                ('duration', models.CharField(default='', max_length=30)),
                ('noSem', models.CharField(default='', max_length=30)),
            ],
        ),
    ]
