# Generated by Django 3.1.2 on 2020-12-26 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EventPlatform', '0004_auto_20201226_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='picture',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
