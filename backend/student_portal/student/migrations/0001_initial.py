# Generated by Django 3.1 on 2020-08-17 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='studentDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mailId', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('Name', models.CharField(default='none', max_length=50)),
                ('DOB', models.CharField(default='none', max_length=50)),
            ],
        ),
    ]
