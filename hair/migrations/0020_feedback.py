# Generated by Django 4.2.5 on 2023-09-10 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hair', '0019_records_time_create'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, verbose_name='Введите ваше имя')),
                ('email', models.EmailField(max_length=254, verbose_name='Введите вашу почту')),
                ('text', models.TextField(verbose_name='Введите ваши пожелания и какие улучшения вы хотели бы видеть в наших Барбершопах')),
            ],
        ),
    ]
