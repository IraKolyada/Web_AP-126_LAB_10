# Generated by Django 4.2.1 on 2024-09-20 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spanner', '0003_alter_spanner_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spanner',
            name='is_published',
            field=models.BooleanField(choices=[(0, 'Черновик'), (1, 'Опубликовано')], default=0),
        ),
    ]
