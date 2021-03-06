# Generated by Django 3.1.2 on 2020-11-01 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Startups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startup_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('team_size', models.IntegerField()),
                ('stage', models.CharField(max_length=200)),
                ('year_formed', models.IntegerField()),
                ('industry', models.CharField(max_length=200)),
                ('startup_description', models.TextField()),
                ('pitch_link', models.URLField()),
                ('website_link', models.URLField()),
            ],
        ),
    ]
