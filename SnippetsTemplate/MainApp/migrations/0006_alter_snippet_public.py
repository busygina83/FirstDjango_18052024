# Generated by Django 5.0.6 on 2024-06-09 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0005_rename_is_public_snippet_public'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='public',
            field=models.BooleanField(),
        ),
    ]
