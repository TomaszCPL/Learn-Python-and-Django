# Generated by Django 2.0 on 2017-12-11 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_profile_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
