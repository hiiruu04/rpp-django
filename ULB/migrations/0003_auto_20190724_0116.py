# Generated by Django 2.2.3 on 2019-07-24 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ULB', '0002_dataset'),
    ]

    operations = [
        migrations.CreateModel(
            name='ULBdata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Time', models.IntegerField()),
                ('V1', models.FloatField()),
                ('V2', models.FloatField()),
                ('V3', models.FloatField()),
                ('V4', models.FloatField()),
                ('V5', models.FloatField()),
                ('V6', models.FloatField()),
                ('V7', models.FloatField()),
                ('V8', models.FloatField()),
                ('V9', models.FloatField()),
                ('V10', models.FloatField()),
                ('V11', models.FloatField()),
                ('V12', models.FloatField()),
                ('V13', models.FloatField()),
                ('V14', models.FloatField()),
                ('V15', models.FloatField()),
                ('V16', models.FloatField()),
                ('V17', models.FloatField()),
                ('V18', models.FloatField()),
                ('V19', models.FloatField()),
                ('V20', models.FloatField()),
                ('V21', models.FloatField()),
                ('V22', models.FloatField()),
                ('V23', models.FloatField()),
                ('V24', models.FloatField()),
                ('V25', models.FloatField()),
                ('V26', models.FloatField()),
                ('V27', models.FloatField()),
                ('V28', models.FloatField()),
                ('Class', models.IntegerField(choices=[(0, 0), (1, 1)])),
            ],
        ),
        migrations.RenameField(
            model_name='ulbdatalabelled',
            old_name='Class',
            new_name='Detect',
        ),
    ]
