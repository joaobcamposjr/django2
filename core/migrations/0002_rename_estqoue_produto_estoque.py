# Generated by Django 4.1.5 on 2023-01-20 02:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produto',
            old_name='estqoue',
            new_name='estoque',
        ),
    ]
