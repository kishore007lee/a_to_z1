# Generated by Django 3.2.7 on 2021-09-16 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('A_to_Z', '0003_auto_20210916_1217'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='shop_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]