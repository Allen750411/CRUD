# Generated by Django 5.1.4 on 2024-12-08 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('skill', models.CharField(max_length=200, null=True)),
                ('content', models.TextField(max_length=300, null=True)),
            ],
        ),
    ]
