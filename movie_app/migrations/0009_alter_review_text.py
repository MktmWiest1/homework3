# Generated by Django 4.0.2 on 2022-02-18 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0008_review_stars_alter_review_movie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='text',
            field=models.TextField(null=True),
        ),
    ]
