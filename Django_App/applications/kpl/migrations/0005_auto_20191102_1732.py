# Generated by Django 2.2.6 on 2019-11-02 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kpl', '0004_auto_20191102_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='earned_points',
            field=models.IntegerField(default=0),
        ),
    ]
