# Generated by Django 4.0.1 on 2022-04-23 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0009_rename_user_student_userid_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='level',
        ),
    ]
