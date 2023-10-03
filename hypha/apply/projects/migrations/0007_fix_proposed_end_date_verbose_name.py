# Generated by Django 2.0.13 on 2019-08-07 08:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("application_projects", "0006_add_project_paf_fields"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="proposed_end",
            field=models.DateTimeField(null=True, verbose_name="Proposed End Date"),
        ),
    ]
