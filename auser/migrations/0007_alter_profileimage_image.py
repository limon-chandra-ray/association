# Generated by Django 4.0.4 on 2022-05-28 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auser', '0006_alter_profilebackgroundimage_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileimage',
            name='image',
            field=models.ImageField(default='deafult_user.png', upload_to='profile'),
        ),
    ]
