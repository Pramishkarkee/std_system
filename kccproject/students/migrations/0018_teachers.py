# Generated by Django 2.2.11 on 2020-04-05 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0017_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coursename', models.CharField(default='', max_length=50)),
                ('semNo', models.CharField(default='', max_length=50)),
                ('firstname', models.CharField(default='', max_length=50)),
                ('lname', models.CharField(default='', max_length=50)),
                ('emailAdd', models.CharField(default='', max_length=50)),
                ('contactNo', models.CharField(default='', max_length=50)),
                ('age', models.CharField(default='', max_length=50)),
                ('gender', models.CharField(default='', max_length=50)),
                ('tmpAdd', models.CharField(default='', max_length=50)),
                ('parAdd', models.CharField(default='', max_length=50)),
                ('timeTeach', models.CharField(default='', max_length=50)),
                ('subject', models.CharField(default='', max_length=50)),
                ('teacherPic', models.FileField(upload_to='Teacher/')),
            ],
        ),
    ]
