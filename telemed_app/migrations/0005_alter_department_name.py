# Generated by Django 4.2.16 on 2024-12-05 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telemed_app', '0004_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
