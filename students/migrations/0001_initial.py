# Generated by Django 3.2.9 on 2021-11-14 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_name', models.CharField(max_length=100)),
                ('s_major', models.CharField(max_length=100)),
                ('s_age', models.IntegerField(default=0)),
                ('s_grade', models.IntegerField(default=0)),
                ('s_gender', models.CharField(max_length=30)),
            ],
        ),
    ]
