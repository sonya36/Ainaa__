# Generated by Django 4.1.1 on 2022-09-15 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('userId', models.AutoField(primary_key=True, serialize=False)),
                ('firstName', models.CharField(default='', max_length=50)),
                ('lastName', models.CharField(default='', max_length=50)),
                ('gender', models.CharField(default='', max_length=10)),
                ('email', models.EmailField(default='', max_length=50)),
                ('password', models.CharField(default='', max_length=20)),
            ],
        ),
    ]
