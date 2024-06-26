# Generated by Django 4.2.11 on 2024-03-21 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("newspaper", "0002_rename_topics_newspaper_topic"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="newspaper",
            options={"ordering": ["-published_date"]},
        ),
        migrations.AlterField(
            model_name="newspaper",
            name="published_date",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
