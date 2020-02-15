# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-29 09:34


from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Center',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('lat', models.CharField(max_length=100)),
                ('lng', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('vicinity', models.CharField(max_length=100)),
                ('place_id', models.CharField(max_length=100)),
                ('types', models.CharField(max_length=100)),
                ('did', models.CharField(max_length=10)),
                ('typeof', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Citizen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('age', models.CharField(max_length=100)),
                ('lat', models.CharField(max_length=100)),
                ('lng', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Copy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('lat', models.CharField(max_length=100)),
                ('lng', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('vicinity', models.CharField(max_length=100)),
                ('place_id', models.CharField(max_length=100)),
                ('types', models.CharField(max_length=100)),
                ('did', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('time', models.CharField(max_length=150)),
                ('lat', models.CharField(max_length=100)),
                ('lng', models.CharField(max_length=100)),
                ('type_of', models.CharField(max_length=100)),
                ('radius', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cid', models.CharField(max_length=100)),
                ('current_status', models.CharField(max_length=100)),
                ('capacity', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=100)),
                ('body', models.CharField(max_length=100)),
                ('message_id', models.CharField(max_length=100)),
                ('created', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Victim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=150)),
                ('pic_id', models.CharField(max_length=65)),
            ],
        ),
    ]
