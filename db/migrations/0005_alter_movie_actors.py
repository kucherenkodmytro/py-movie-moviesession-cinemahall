# Generated by Django 4.0.2 on 2023-10-16 13:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("db", "0004_alter_movie_actors_alter_movie_genres"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="actors",
            field=models.ManyToManyField(related_name="movies", to="db.Actor"),
        ),
    ]