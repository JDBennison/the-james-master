# Generated by Django 3.1.6 on 2021-03-02 00:20

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blogpost_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='body',
            field=tinymce.models.HTMLField(),
        ),
    ]