# Generated by Django 2.0.3 on 2018-11-12 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='plot',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='tv',
            name='plot',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
