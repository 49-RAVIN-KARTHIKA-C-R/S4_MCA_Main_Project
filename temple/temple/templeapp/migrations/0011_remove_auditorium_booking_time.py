# Generated by Django 3.2.10 on 2022-07-13 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('templeapp', '0010_remove_committe_program_committee_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auditorium_booking',
            name='time',
        ),
    ]
