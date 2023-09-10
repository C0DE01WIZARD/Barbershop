# Generated by Django 3.2.16 on 2023-09-07 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hair', '0010_auto_20230907_1918'),
    ]

    operations = [
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField(max_length=25, verbose_name='Время записи')),
            ],
        ),
        migrations.AlterField(
            model_name='barber',
            name='name',
            field=models.CharField(max_length=20, verbose_name='Имя барбера'),
        ),
        migrations.AlterField(
            model_name='records',
            name='datetime',
            field=models.DateTimeField(verbose_name='Время и дата'),
        ),
    ]