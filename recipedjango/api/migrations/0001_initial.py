# Generated by Django 4.0.5 on 2022-10-07 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='base',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domainName', models.CharField(max_length=200)),
                ('ipAddr', models.CharField(max_length=200)),
            ],
        ),
    ]
