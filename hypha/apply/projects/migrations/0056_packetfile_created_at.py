# Generated by Django 3.2.16 on 2022-10-13 10:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("application_projects", "0055_alter_project_status_add_pafreviewersrole"),
    ]

    operations = [
        migrations.AddField(
            model_name="packetfile",
            name="created_at",
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
