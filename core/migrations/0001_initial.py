# Generated by Django 2.0.4 on 2018-04-28 14:14

import core.models.toy
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Toy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(db_index=True, default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('changed_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, default='')),
                ('photo', models.ImageField(blank=True, null=True, upload_to=core.models.toy.photos_upload_path)),
                ('type', models.CharField(choices=[('donation', 'Donation'), ('rent', 'Rent'), ('sale', 'Sale')], default='sale', max_length=50)),
                ('owner_name', models.CharField(blank=True, default='', max_length=100)),
                ('owner_phone_number', models.CharField(max_length=100)),
            ],
        ),
    ]
