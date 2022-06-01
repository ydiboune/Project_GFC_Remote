# Generated by Django 2.2.10 on 2022-02-28 08:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scolar', '0193_auto_20220227_1610'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bloc',
            name='bureaux',
        ),
        migrations.AddField(
            model_name='bureau',
            name='bloc',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='bureaux', to='scolar.Bloc'),
        ),
    ]
