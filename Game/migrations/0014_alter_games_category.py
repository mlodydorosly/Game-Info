# Generated by Django 3.2.7 on 2021-11-02 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Game', '0013_games_gry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='games',
            name='category',
            field=models.ManyToManyField(null=True, to='Game.Category', verbose_name='list of sites'),
        ),
    ]
