# Generated by Django 4.2.9 on 2024-06-01 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0002_item_item_des_item_item_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://alllocal.ca/wp-content/uploads/2020/11/food-placeholder.png', max_length=500),
        ),
    ]
