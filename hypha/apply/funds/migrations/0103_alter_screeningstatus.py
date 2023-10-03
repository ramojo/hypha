# Generated by Django 3.2.15 on 2022-09-14 05:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("funds", "0102_add_projectapprovalform_to_fundbase_labbase"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="screeningstatus",
            options={
                "verbose_name": "Screening Decision",
                "verbose_name_plural": "screening decisions",
            },
        ),
        migrations.AlterField(
            model_name="screeningstatus",
            name="default",
            field=models.BooleanField(
                default=False,
                help_text="Only one Yes and No screening decision can be set as default.",
                verbose_name="Default Yes/No",
            ),
        ),
    ]
