# Generated by Django 4.1.7 on 2023-03-10 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='user',
            field=models.CharField(max_length=100),
        ),
    ]
