# Generated by Django 2.0.4 on 2018-04-20 08:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('query_learn', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='blog',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='query_learn.Blog'),
            preserve_default=False,
        ),
    ]
