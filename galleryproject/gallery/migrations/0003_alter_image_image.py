# Generated by Django 4.0.4 on 2022-05-29 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_image_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to=''),
        ),
    ]
