# Generated by Django 4.2.5 on 2024-04-21 14:16

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0002_alter_recipe_intro_alter_recipe_owner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recipe',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='recipe',
            name='vote_ratio',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='vote_total',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('body', models.TextField(blank=True, null=True)),
                ('value', models.CharField(choices=[('up', 'Up Vote'), ('down', 'Down Vote')], max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogue.profile')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogue.recipe')),
            ],
            options={
                'unique_together': {('owner', 'recipe')},
            },
        ),
    ]