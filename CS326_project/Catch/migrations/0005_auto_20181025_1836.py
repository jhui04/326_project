# Generated by Django 2.1.2 on 2018-10-25 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Catch', '0004_auto_20181020_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='petuser',
            name='location',
            field=models.FloatField(max_length=30),
        ),
    ]
