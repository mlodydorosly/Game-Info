# Generated by Django 3.2.7 on 2021-11-02 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Game', '0007_alter_games_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='games',
            name='category',
        ),
        migrations.AddField(
            model_name='games',
            name='category',
            field=models.ManyToManyField(null=True, to='Game.Category'),
        ),
    ]
