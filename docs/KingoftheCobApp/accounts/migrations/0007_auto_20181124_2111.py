# Generated by Django 2.0.1 on 2018-11-25 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20181123_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='requestor',
            field=models.GenericIPAddressField(default='1.1.1.1'),
        ),
        migrations.AlterField(
            model_name='event',
            name='requestor',
            field=models.GenericIPAddressField(default='1.1.1.1'),
        ),
    ]
