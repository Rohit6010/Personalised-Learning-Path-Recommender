# Generated by Django 3.1.6 on 2022-04-25 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0007_auto_20220414_2356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='practice',
            name='subTopic',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
