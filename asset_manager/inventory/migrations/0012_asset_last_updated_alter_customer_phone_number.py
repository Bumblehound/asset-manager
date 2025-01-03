# Generated by Django 5.1.4 on 2025-01-02 22:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0011_alter_customer_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='last_updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must start with an optional '+' followed by digits, with optional spaces, parentheses, or hyphens.", regex='^\\+?(\\(\\d{1,4}\\)|\\d{1,4})?[\\s\\-]?\\d{1,4}[\\s\\-]?\\d{1,4}[\\s\\-]?\\d{1,4}$')]),
        ),
    ]