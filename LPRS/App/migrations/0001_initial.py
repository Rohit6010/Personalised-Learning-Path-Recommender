# Generated by Django 3.1.6 on 2022-03-27 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SignUp',
            fields=[
                ('userId', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(default='', max_length=50)),
                ('email', models.EmailField(default='', max_length=50)),
                ('password', models.CharField(default='', max_length=50)),
                ('phone', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_name', models.CharField(max_length=50)),
                ('question', models.CharField(max_length=100)),
                ('option1', models.CharField(max_length=100)),
                ('option2', models.CharField(max_length=100)),
                ('option3', models.CharField(max_length=100)),
                ('option4', models.CharField(max_length=100)),
                ('answer', models.CharField(max_length=100)),
                ('level', models.CharField(max_length=100)),
            ],
        ),
    ]