# Generated by Django 3.1.6 on 2022-03-27 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_auto_20220327_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='linkedlist',
            name='question',
            field=models.CharField(max_length=500),
        ),
    ]