# Generated by Django 4.2.11 on 2024-03-20 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("newspaper", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="newspaper",
            old_name="topics",
            new_name="topic",
        ),
    ]
