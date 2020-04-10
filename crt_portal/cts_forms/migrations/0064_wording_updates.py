# Generated by Django 2.2.12 on 2020-04-09 21:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cts_forms', '0063_report_primary_statute'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='last_incident_day',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name=django.core.validators.MaxValueValidator(31, message='Please enter a valid day of the month. Day must be between 1 and the last day of the month.')),
        ),
        migrations.AlterField(
            model_name='report',
            name='last_incident_month',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name=django.core.validators.MaxValueValidator(12, message='Please enter a valid month. Month must be between 1 and 12.')),
        ),
        migrations.AlterField(
            model_name='report',
            name='last_incident_year',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name=django.core.validators.MaxValueValidator(2020, message='Date can not be in the future.')),
        ),
        migrations.AlterField(
            model_name='report',
            name='primary_complaint',
            field=models.CharField(choices=[('workplace', 'Workplace discrimination or other employment-related problem'), ('housing', 'Housing discrimination or harassment'), ('education', 'Discrimination at a school, educational program or service, or related to receiving education'), ('voting', 'Voting rights or ability to vote blocked or affected'), ('police', 'Mistreated by police, or correctional staff (including while in prison)'), ('commercial_or_public', 'Discriminated against in a commercial location or public place'), ('something_else', 'Something else happened')], default='', max_length=100),
        ),
    ]
