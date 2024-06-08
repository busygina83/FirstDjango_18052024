# Generated by Django 5.0.6 on 2024-06-08 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='lang',
            field=models.CharField(choices=[('py', 'Python'), ('js', 'JavaScript'), ('cpp', 'C++'), ('html', 'HTML'), ('grv', 'Groovy')], max_length=30),
        ),
    ]
