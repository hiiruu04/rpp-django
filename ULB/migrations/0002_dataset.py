# Generated by Django 2.2.3 on 2019-07-22 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ULB', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dataset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('File', models.FileField(upload_to='dataset/ulb/')),
            ],
        ),
    ]
