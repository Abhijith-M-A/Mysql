# Generated by Django 3.2.2 on 2021-07-17 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('databaser', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Billnonpayers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temp5', models.CharField(max_length=200)),
            ],
        ),
    ]
