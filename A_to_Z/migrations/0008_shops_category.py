# Generated by Django 3.2.7 on 2021-09-23 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('A_to_Z', '0007_products_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='shops',
            name='category',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]