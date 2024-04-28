# Generated by Django 4.2.3 on 2023-12-25 17:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HR', '0014_training'),
    ]

    operations = [
        migrations.CreateModel(
            name='Track_Training',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assess', models.TextField(null=True)),
                ('progress', models.IntegerField(default=0)),
                ('emp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HR.emp')),
            ],
        ),
        migrations.RemoveField(
            model_name='training',
            name='req_no',
        ),
        migrations.DeleteModel(
            name='Bank_details',
        ),
        migrations.AddField(
            model_name='track_training',
            name='training',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HR.training'),
        ),
    ]
