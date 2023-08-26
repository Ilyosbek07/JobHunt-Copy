# Generated by Django 4.2.4 on 2023-08-26 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PopularSearch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=255, unique=True)),
                ('count', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
