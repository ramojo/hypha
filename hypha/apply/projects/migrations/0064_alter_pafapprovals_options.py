# Generated by Django 3.2.18 on 2023-03-02 04:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_projects', '0063_projectsettings_paf_approval_sequential'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pafapprovals',
            options={'ordering': ['paf_reviewer_role__sort_order']},
        ),
    ]