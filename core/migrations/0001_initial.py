# Generated by Django 4.0.3 on 2022-03-09 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bg_color', models.CharField(blank=True, choices=[('primary', 'Blue'), ('success', 'Green'), ('danger', 'Red'), ('dark', 'Black'), ('warning', 'Yellow'), ('info', 'Light blue'), ('light', 'Light'), ('White', 'White')], default='White', max_length=20, null=True, verbose_name='Bachground color')),
                ('txt_color', models.CharField(blank=True, choices=[('dark', 'Black'), ('white', 'White')], default='White', max_length=20, null=True, verbose_name='Text color')),
                ('topic', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
