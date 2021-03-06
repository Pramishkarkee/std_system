# Generated by Django 2.2.11 on 2020-04-04 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0012_auto_20200403_0926'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cName', models.CharField(default='', max_length=50)),
                ('Semister', models.CharField(default='', max_length=50)),
                ('firstName', models.CharField(default='', max_length=50)),
                ('lastName', models.CharField(default='', max_length=50)),
                ('emailAdd', models.CharField(default='', max_length=50)),
                ('ContactNo', models.CharField(default='', max_length=50)),
                ('BirthDate', models.DateField()),
                ('gender', models.CharField(default='', max_length=50)),
                ('District', models.CharField(default='', max_length=50)),
                ('village', models.CharField(default='', max_length=50)),
                ('fatherName', models.CharField(default='', max_length=50)),
                ('fatherOccupation', models.CharField(default='', max_length=50)),
                ('motherName', models.CharField(default='', max_length=50)),
                ('motherOccupation', models.CharField(default='', max_length=50)),
                ('parentEmail', models.CharField(default='', max_length=50)),
                ('parentContactNo', models.CharField(default='', max_length=50)),
                ('studentPicture', models.FileField(upload_to='')),
            ],
        ),
    ]
