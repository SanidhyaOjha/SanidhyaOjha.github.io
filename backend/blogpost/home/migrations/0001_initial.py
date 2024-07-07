# Generated by Django 5.0.6 on 2024-07-07 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(verbose_name=100)),
                ('content', models.TextField(default=None)),
                ('author', models.CharField(verbose_name=100)),
                ('timestamp', models.DateTimeField(default=None)),
            ],
        ),
    ]
