# Generated by Django 5.0.6 on 2024-06-09 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0003_snippet_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='is_public',
            field=models.BooleanField(default=True),
        ),
    ]
