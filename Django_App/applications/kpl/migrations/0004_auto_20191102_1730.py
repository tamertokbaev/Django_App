# Generated by Django 2.2.6 on 2019-11-02 11:30

from django.db import migrations, models
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('kpl', '0003_auto_20191102_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='earned_points',
            field=models.IntegerField(default=django.db.models.expressions.CombinedExpression(django.db.models.expressions.F(models.IntegerField(default=0)), '+', django.db.models.expressions.Value(1))),
        ),
    ]
