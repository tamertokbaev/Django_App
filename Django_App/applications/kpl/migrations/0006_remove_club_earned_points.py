# Generated by Django 2.2.6 on 2019-11-02 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kpl', '0005_auto_20191102_1732'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='club',
            name='earned_points',
        ),
    ]
