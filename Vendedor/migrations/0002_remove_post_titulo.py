# Generated by Django 5.1.6 on 2025-03-03 02:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Vendedor', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='titulo',
        ),
    ]
