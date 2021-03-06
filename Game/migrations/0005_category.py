# Generated by Django 3.2.7 on 2021-11-02 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Game', '0004_rename_game_games'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
    ]
