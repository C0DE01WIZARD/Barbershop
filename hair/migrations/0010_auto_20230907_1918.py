# Generated by Django 3.2.16 on 2023-09-07 19:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hair', '0009_news'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='barber',
            options={'verbose_name': 'Барбер', 'verbose_name_plural': 'Барберы'},
        ),
        migrations.AlterModelOptions(
            name='hairstyles',
            options={'verbose_name': 'Прическа', 'verbose_name_plural': 'Прически'},
        ),
        migrations.AlterModelOptions(
            name='records',
            options={'verbose_name': 'Запись', 'verbose_name_plural': 'Записи'},
        ),
        migrations.RemoveField(
            model_name='barber',
            name='types_hairstyle',
        ),
    ]
