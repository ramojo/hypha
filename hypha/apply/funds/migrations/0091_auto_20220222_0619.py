# Generated by Django 2.2.27 on 2022-02-22 06:19

from django.db import migrations


def set_duration_required_false(apps, schema_editor):
    ApplicationSubmission = apps.get_model('funds', 'ApplicationSubmission')
    for submission in ApplicationSubmission.objects.all():
        for id, struct_child in enumerate(submission.form_fields):
            struct_value = struct_child.value
            if struct_value['field_label'] == 'Duration' and struct_value['required'] is None:
                submission.form_fields[id].value['required'] = False
                submission.save()


class Migration(migrations.Migration):

    dependencies = [
        ('funds', '0090_auto_20220218_1208'),
    ]

    operations = [
        migrations.RunPython(set_duration_required_false)
    ]
