# Generated by Django 4.1.7 on 2023-03-12 06:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0003_remove_company_employees_device_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='devicelog',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='asset.company'),
        ),
    ]
