# Generated by Django 3.2 on 2023-03-01 22:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("polls", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="choice",
            name="id",
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID"),
        ),
        migrations.AlterField(
            model_name="question",
            name="id",
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID"),
        ),
    ]
