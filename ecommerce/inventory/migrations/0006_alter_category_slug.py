# Generated by Django 5.0.6 on 2024-06-20 07:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("inventory", "0005_alter_category_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="slug",
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
