# Generated by Django 4.2.16 on 2024-12-03 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telemed_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=10)),
                ('message', models.TextField()),
            ],
        ),
    ]