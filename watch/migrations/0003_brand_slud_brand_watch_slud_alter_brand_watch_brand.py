# Generated by Django 4.2 on 2023-05-19 07:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('watch', '0002_brand_watch'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='slud',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='brand_watch',
            name='slud',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='brand_watch',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='watch', to='watch.brand'),
        ),
    ]