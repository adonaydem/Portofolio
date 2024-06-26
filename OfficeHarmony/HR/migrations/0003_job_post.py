# Generated by Django 4.2.3 on 2023-12-24 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HR', '0002_emp_email_alter_emp_birthdate_alter_emp_startdate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job_Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postion', models.CharField(max_length=255)),
                ('department', models.CharField(max_length=255)),
                ('no_applicants', models.IntegerField()),
                ('no_positions', models.IntegerField()),
                ('description', models.TextField()),
                ('startdate', models.DateField()),
                ('enddate', models.DateField()),
                ('review_startdate', models.DateField()),
                ('onboarding_date', models.DateField()),
            ],
        ),
    ]
