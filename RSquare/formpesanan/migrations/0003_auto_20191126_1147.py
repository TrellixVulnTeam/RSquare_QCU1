# Generated by Django 2.2.2 on 2019-11-26 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formpesanan', '0002_auto_20191126_1138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pesanan',
            name='product',
        ),
        migrations.AddField(
            model_name='pesanan',
            name='id_product',
            field=models.IntegerField(default=0),
        ),
    ]
