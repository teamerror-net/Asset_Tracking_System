# Generated by Django 4.1.7 on 2023-03-12 06:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0002_alter_employee_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='employees',
        ),
        migrations.AddField(
            model_name='device',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='asset.company'),
        ),
    ]