# Generated by Django 5.1.4 on 2025-01-10 07:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_movieinfo_poster'),
    ]

    operations = [
        migrations.CreateModel(
            name='CensorInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(max_length=10, null=True)),
                ('certified', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='movieinfo',
            name='censor_details',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='movie', to='movies.censorinfo'),
        ),
    ]
