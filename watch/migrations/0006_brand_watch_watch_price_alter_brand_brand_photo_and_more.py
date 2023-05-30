# Generated by Django 4.2 on 2023-05-19 19:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('watch', '0005_brand_brand_photo_brand_watch_watch_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand_watch',
            name='watch_price',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='brand',
            name='brand_photo',
            field=models.ImageField(default='', upload_to='brand-img'),
        ),
        migrations.AlterField(
            model_name='brand_watch',
            name='watch_photo',
            field=models.ImageField(default='', upload_to='watch-img'),
        ),
    ]
