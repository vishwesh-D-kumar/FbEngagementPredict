# Generated by Django 2.2.3 on 2019-07-08 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mainsite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('siteurl', models.CharField(max_length=100)),
                ('crawled', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Subsites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subsiteurl', models.CharField(max_length=1000)),
                ('mainsite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FBEngagementPredict.Mainsite')),
            ],
        ),
    ]
