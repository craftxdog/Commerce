# Generated by Django 4.2.1 on 2023-05-26 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='email address'),
        ),
    ]
