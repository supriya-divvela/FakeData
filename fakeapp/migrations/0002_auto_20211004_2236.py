# Generated by Django 3.2.6 on 2021-10-04 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fakeapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='address',
        ),
        migrations.AlterField(
            model_name='employee',
            name='salary',
            field=models.IntegerField(),
        ),
    ]
