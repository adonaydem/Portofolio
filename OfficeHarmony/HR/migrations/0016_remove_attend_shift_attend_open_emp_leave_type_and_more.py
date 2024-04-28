# Generated by Django 4.2.3 on 2023-12-26 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HR', '0015_track_training_remove_training_req_no_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attend',
            name='shift',
        ),
        migrations.AddField(
            model_name='attend',
            name='open',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='emp',
            name='leave_type',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='emp',
            name='on_leave',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='WorkHour',
        ),
    ]