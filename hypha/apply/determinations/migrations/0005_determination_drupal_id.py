# Generated by Django 2.0.2 on 2018-08-29 17:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("determinations", "0004_change_labels"),
    ]

    operations = [
        migrations.AddField(
            model_name="determination",
            name="drupal_id",
            field=models.IntegerField(blank=True, editable=False, null=True),
        ),
    ]
