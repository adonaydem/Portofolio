# Generated by Django 4.2.3 on 2023-12-27 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HR', '0018_request'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='req_name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
