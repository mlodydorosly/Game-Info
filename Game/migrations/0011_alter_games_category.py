# Generated by Django 3.2.7 on 2021-11-02 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Game', '0010_alter_games_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='games',
            name='category',
            field=models.ManyToManyField(to='Game.Category', verbose_name='list of sites'),
        ),
    ]
