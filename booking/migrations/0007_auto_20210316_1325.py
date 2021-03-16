# Generated by Django 3.1.6 on 2021-03-16 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0006_auto_20210316_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_booked',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='booking.booking'),
        ),
        migrations.AlterField(
            model_name='order',
            name='service',
            field=models.CharField(choices=[('IN', 'Introduction To DnD'), ('OS', 'One Shot Adventure'), ('OC', 'Ongoing Campaign')], max_length=2, null=True),
        ),
    ]
