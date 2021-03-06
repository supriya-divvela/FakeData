# Generated by Django 3.2.6 on 2021-10-04 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('job', models.CharField(max_length=30)),
                ('salary', models.FloatField()),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=30)),
            ],
        ),
    ]
