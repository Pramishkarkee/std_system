# Generated by Django 3.0 on 2019-12-31 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=30)),
                ('password', models.CharField(default='', max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='student',
            name='password',
        ),
        migrations.RemoveField(
            model_name='student',
            name='username',
        ),
        migrations.AddField(
            model_name='student',
            name='S_contact_no',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='student',
            name='S_faculty',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='student',
            name='S_id',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='student',
            name='S_name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='student',
            name='S_parents_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
