# Generated by Django 3.2.5 on 2021-09-02 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='eventform',
            name='event_name',
            field=models.CharField(max_length=40),
        ),
    ]
