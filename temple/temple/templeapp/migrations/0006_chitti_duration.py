# Generated by Django 3.2.10 on 2022-07-04 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('templeapp', '0005_auto_20220704_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='chitti',
            name='duration',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
