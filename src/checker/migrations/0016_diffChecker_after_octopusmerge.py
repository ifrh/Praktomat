# Generated by Django 2.2.11 on 2020-03-16 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checker', '0015_mergeKITPraktomat2020_octopus_hbrs_extensions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diffchecker',
            name='order',
            field=models.IntegerField(help_text='Determines the order in which the checker will start. Not necessary continuously!'),
        ),
    ]
