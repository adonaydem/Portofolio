# Generated by Django 4.2.3 on 2023-12-24 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HR', '0008_applicant_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='interview',
            field=models.TextField(null=True),
        ),
    ]
