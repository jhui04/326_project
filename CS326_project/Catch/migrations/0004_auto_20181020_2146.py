# Generated by Django 2.1.2 on 2018-10-21 01:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Catch', '0003_pet_pet_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='description',
            field=models.TextField(default=' '),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='pet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Catch.Pet'),
        ),
    ]
