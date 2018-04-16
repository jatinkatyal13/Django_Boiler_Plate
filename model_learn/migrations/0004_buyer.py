# Generated by Django 2.0.4 on 2018-04-16 10:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model_learn', '0003_auto_20180416_1034'),
    ]

    operations = [
        migrations.CreateModel(
            name='buyer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=200, validators=[django.core.validators.EmailValidator])),
            ],
        ),
    ]
