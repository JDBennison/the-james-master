# Generated by Django 3.1.6 on 2021-03-10 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_auto_20210310_2309'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='players',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
