# Generated by Django 5.0.5 on 2024-05-07 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bloger', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blodpost',
            options={'verbose_name': 'блог', 'verbose_name_plural': 'Блог'},
        ),
        migrations.AlterModelOptions(
            name='blogers',
            options={'verbose_name': 'коммент', 'verbose_name_plural': 'Коммент'},
        ),
        migrations.RemoveField(
            model_name='blogers',
            name='date',
        ),
    ]
