# Generated by Django 3.2.7 on 2021-11-02 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Game', '0008_auto_20211102_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='games',
            name='category',
            field=models.ManyToManyField(to='Game.Category', verbose_name='list of sites'),
        ),
    ]