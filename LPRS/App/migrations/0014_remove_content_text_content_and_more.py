# Generated by Django 4.0.1 on 2022-04-23 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0013_student_curr_topic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='text_content',
        ),
        migrations.RemoveField(
            model_name='content',
            name='video_content',
        ),
        migrations.AddField(
            model_name='content',
            name='text1',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='text2',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='text3',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='text4',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='video1',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='video2',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='video3',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='video4',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
    ]