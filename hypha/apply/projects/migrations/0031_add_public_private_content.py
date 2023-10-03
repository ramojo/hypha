# Generated by Django 2.1.11 on 2019-10-31 22:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("application_projects", "0030_report_skipped"),
    ]

    operations = [
        migrations.RenameField(
            model_name="reportversion",
            old_name="content",
            new_name="public_content",
        ),
        migrations.RemoveField(
            model_name="report",
            name="public",
        ),
        migrations.AddField(
            model_name="reportversion",
            name="private_content",
            field=models.TextField(default=""),
            preserve_default=False,
        ),
    ]
