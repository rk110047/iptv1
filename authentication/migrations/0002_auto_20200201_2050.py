# Generated by Django 3.0 on 2020-02-01 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='parental_lock',
            field=models.IntegerField(default=6666),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='recording_time',
            field=models.IntegerField(default=30),
        ),
    ]
