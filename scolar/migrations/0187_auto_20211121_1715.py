# Generated by Django 2.2.10 on 2021-11-21 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scolar', '0186_auto_20211121_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avance',
            name='encours',
            field=models.BooleanField(blank=True, default='False'),
        ),
    ]
