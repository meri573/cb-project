# Generated by Django 4.0.3 on 2022-06-03 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('point_site', '0002_points_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='points',
            name='points',
            field=models.IntegerField(default=150),
        ),
    ]