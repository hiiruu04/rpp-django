# Generated by Django 2.1.7 on 2019-04-30 07:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('random_forest', '0013_auto_20190429_1036'),
    ]

    operations = [
        migrations.AddField(
            model_name='hyperparameterrf',
            name='dataset',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='random_forest.Dataset'),
        ),
    ]