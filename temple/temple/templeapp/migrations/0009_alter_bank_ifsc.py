# Generated by Django 3.2.10 on 2022-07-06 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('templeapp', '0008_winner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bank',
            name='ifsc',
            field=models.CharField(max_length=100),
        ),
    ]
