# Generated by Django 4.1.1 on 2022-09-21 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_api', '0004_alter_check_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='check',
            name='isHere',
            field=models.BooleanField(default=False),
        ),
    ]
