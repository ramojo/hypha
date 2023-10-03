# Generated by Django 2.2.24 on 2021-12-07 20:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("application_projects", "0043_remove_project_approval_form"),
    ]

    operations = [
        migrations.AlterField(
            model_name="invoice",
            name="status",
            field=models.TextField(
                choices=[
                    ("submitted", "Submitted"),
                    ("changes_requested", "Changes Requested"),
                    ("approved_by_staff", "Approved by staff"),
                    ("approved_by_finance1", "Approved By Finance 1"),
                    ("approved_by_finance2", "Approved By Finance 2"),
                    ("resubmitted", "Resubmitted"),
                    ("paid", "Paid"),
                    ("declined", "Declined"),
                ],
                default="submitted",
            ),
        ),
    ]
