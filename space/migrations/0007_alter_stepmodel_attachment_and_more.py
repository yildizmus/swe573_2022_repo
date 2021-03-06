# Generated by Django 4.0.4 on 2022-05-22 20:51

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('space', '0006_stepmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stepmodel',
            name='attachment',
            field=models.FileField(blank=True, null=True, upload_to='files'),
        ),
        migrations.AlterField(
            model_name='stepmodel',
            name='stepcontent',
            field=ckeditor.fields.RichTextField(max_length=500),
        ),
    ]
