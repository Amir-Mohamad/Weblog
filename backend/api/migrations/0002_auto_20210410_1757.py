# Generated by Django 3.1.7 on 2021-04-10 17:57

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
