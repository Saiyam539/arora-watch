# Generated by Django 4.2 on 2023-05-19 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watch', '0004_remove_brand_slud_remove_brand_watch_slud'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='brand_photo',
            field=models.ImageField(default=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='brand_watch',
            name='watch_photo',
            field=models.ImageField(default=True, upload_to=''),
        ),
    ]
