# Generated by Django 4.2.1 on 2024-09-20 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spanner', '0002_alter_spanner_options_spanner_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spanner',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]
