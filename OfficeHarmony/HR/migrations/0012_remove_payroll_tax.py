# Generated by Django 4.2.3 on 2023-12-25 06:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HR', '0011_payroll_retirement'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payroll',
            name='tax',
        ),
    ]