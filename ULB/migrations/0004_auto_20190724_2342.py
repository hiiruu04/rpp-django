# Generated by Django 2.2.3 on 2019-07-24 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ULB', '0003_auto_20190724_0116'),
    ]

    operations = [
        migrations.AddField(
            model_name='ulbdata',
            name='Amount',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ulbdatalabelled',
            name='Amount',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
