# Generated by Django 2.0.4 on 2018-04-16 11:04

from django.db import migrations, models
import model_learn.models


class Migration(migrations.Migration):

    dependencies = [
        ('model_learn', '0011_buyer_dp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyer',
            name='dp',
            field=models.ImageField(null=True, upload_to=model_learn.models.upload_image),
        ),
    ]
