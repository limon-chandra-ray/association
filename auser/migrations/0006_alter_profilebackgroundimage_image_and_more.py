# Generated by Django 4.0.4 on 2022-05-27 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auser', '0005_profileimage_profilebackgroundimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilebackgroundimage',
            name='image',
            field=models.ImageField(default='water-dropsjpg.jpg', upload_to='profile'),
        ),
        migrations.AlterField(
            model_name='profileimage',
            name='image',
            field=models.ImageField(default='default_user.png', upload_to='profile'),
        ),
    ]
