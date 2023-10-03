# Generated by Django 2.0.13 on 2019-08-12 15:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import hypha.apply.projects.models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("application_projects", "0012_adjust_storage_class"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contract",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "file",
                    models.FileField(
                        upload_to=hypha.apply.projects.models.project.contract_path
                    ),
                ),
                ("is_signed", models.BooleanField("Signed?", default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "approver",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="contracts",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="contracts",
                        to="application_projects.Project",
                    ),
                ),
            ],
        ),
    ]
