# Generated by Django 3.2.10 on 2022-07-08 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('templeapp', '0009_alter_bank_ifsc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='committe_program',
            name='committee_id',
        ),
    ]
