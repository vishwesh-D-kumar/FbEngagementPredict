# Generated by Django 2.2.3 on 2019-07-08 13:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('FBEngagementPredict', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainsite',
            name='lastcrawled',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
