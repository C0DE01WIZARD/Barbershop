# Generated by Django 4.2.3 on 2023-07-31 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hairstyles',
            name='description',
            field=models.TextField(default='default title', max_length=255, verbose_name='Описание прически'),
        ),
    ]