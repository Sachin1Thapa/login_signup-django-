# Generated by Django 5.0.1 on 2024-02-05 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('img', models.ImageField(upload_to='img')),
                ('author', models.CharField(default='Sachin', max_length=20)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('desc', models.TextField(default='Available in List library')),
            ],
        ),
    ]