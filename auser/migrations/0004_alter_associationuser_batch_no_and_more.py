# Generated by Django 4.0.4 on 2022-05-15 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auser', '0003_alter_associationuser_batch_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='associationuser',
            name='batch_no',
            field=models.CharField(max_length=40, verbose_name='batch no'),
        ),
        migrations.AlterField(
            model_name='associationuser',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='email address'),
        ),
    ]
