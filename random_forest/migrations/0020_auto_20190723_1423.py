# Generated by Django 2.2.3 on 2019-07-23 07:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('random_forest', '0019_auto_20190619_1950'),
    ]

    operations = [
        migrations.RenameField(
            model_name='randomforest',
            old_name='k_cv',
            new_name='test_prosentase',
        ),
        migrations.RenameField(
            model_name='setlabel',
            old_name='nilai_label_kanker',
            new_name='nilai_label_fraud',
        ),
    ]
