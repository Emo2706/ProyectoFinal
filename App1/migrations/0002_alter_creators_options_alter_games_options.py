# Generated by Django 4.0.4 on 2022-05-26 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='creators',
            options={'verbose_name': 'Creators', 'verbose_name_plural': 'Creators'},
        ),
        migrations.AlterModelOptions(
            name='games',
            options={'verbose_name': 'Games', 'verbose_name_plural': 'Games'},
        ),
    ]
