# Generated by Django 4.2.3 on 2023-12-24 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HR', '0004_rename_postion_job_post_position'),
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=64)),
                ('lname', models.CharField(max_length=64)),
                ('email', models.CharField(default='ex@g.c', max_length=64)),
            ],
        ),
    ]
