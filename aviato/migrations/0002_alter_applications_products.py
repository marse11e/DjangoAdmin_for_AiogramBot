# Generated by Django 4.1.7 on 2023-03-07 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aviato', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applications',
            name='products',
            field=models.ManyToManyField(to='aviato.products', verbose_name='Привязанный товар'),
        ),
    ]
