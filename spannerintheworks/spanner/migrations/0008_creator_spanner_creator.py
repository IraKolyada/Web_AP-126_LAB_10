# Generated by Django 4.2.1 on 2024-09-21 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spanner', '0007_tagpost_alter_spanner_cat_spanner_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Creator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='spanner',
            name='creator',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='creater', to='spanner.creator'),
        ),
    ]
