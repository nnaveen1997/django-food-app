# Generated by Django 4.0.3 on 2022-03-19 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfoodapp', '0005_alter_image_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='img',
        ),
        migrations.AlterField(
            model_name='image',
            name='img_url',
            field=models.ImageField(upload_to=''),
        ),
    ]
