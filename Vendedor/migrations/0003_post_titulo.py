# Generated by Django 5.1.6 on 2025-03-05 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vendedor', '0002_remove_post_titulo'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='titulo',
            field=models.CharField(default='', max_length=100),
        ),
    ]
