# Generated by Django 2.0.1 on 2018-11-28 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_task_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='current_state',
            field=models.CharField(choices=[('unscheduled', 'unscheduled'), ('unstarted', 'unstarted'), ('started', 'started'), ('rejected', 'rejected'), ('finished', 'finished'), ('delivered', 'delivered'), ('accepted', 'accepted')], default='unscheduled', max_length=20),
        ),
    ]
