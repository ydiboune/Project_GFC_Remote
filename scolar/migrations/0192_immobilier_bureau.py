# Generated by Django 2.2.10 on 2022-02-22 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scolar', '0191_immobilier_bloc'),
    ]

    operations = [
        migrations.AddField(
            model_name='immobilier',
            name='bureau',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='scolar.Bureau'),
        ),
    ]
