# Generated by Django 2.1.11 on 2019-10-31 09:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("application_projects", "0028_report_draft"),
    ]

    operations = [
        migrations.AddField(
            model_name="report",
            name="submitted",
            field=models.DateTimeField(null=True),
        ),
    ]
