# Generated by Django 4.1.4 on 2023-01-18 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Outpass',
            fields=[
                ('username', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('roll', models.CharField(max_length=15)),
                ('Hostel', models.CharField(max_length=25)),
                ('Reason', models.CharField(max_length=1000)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('Phone_no', models.IntegerField()),
                ('duration', models.IntegerField()),
            ],
        ),
    ]
