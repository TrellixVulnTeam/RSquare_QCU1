# Generated by Django 2.2.2 on 2019-11-27 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ListPesanan', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listpesananpage',
            name='alamat',
        ),
        migrations.RemoveField(
            model_name='listpesananpage',
            name='email',
        ),
        migrations.RemoveField(
            model_name='listpesananpage',
            name='harga',
        ),
        migrations.RemoveField(
            model_name='listpesananpage',
            name='nama',
        ),
        migrations.RemoveField(
            model_name='listpesananpage',
            name='nama_barang',
        ),
        migrations.RemoveField(
            model_name='listpesananpage',
            name='no_wa',
        ),
    ]