# Generated by Django 3.1.2 on 2020-12-04 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startups', '0002_auto_20201204_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='startup',
            name='pitch_link',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='startup',
            name='website_link',
            field=models.URLField(blank=True),
        ),
    ]
