# Generated by Django 4.2.5 on 2024-04-21 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0003_alter_recipe_options_recipe_vote_ratio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='value',
            field=models.CharField(choices=[('up', 'Up Vote'), ('down', 'Down Vote')], default='', max_length=200),
        ),
    ]