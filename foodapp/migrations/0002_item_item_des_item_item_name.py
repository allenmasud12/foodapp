# Generated by Django 4.2.13 on 2024-05-31 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_des',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='item',
            name='item_name',
            field=models.CharField(default='', max_length=200),
        ),
    ]
