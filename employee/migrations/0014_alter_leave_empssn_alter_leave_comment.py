# Generated by Django 4.1.4 on 2022-12-29 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0013_leave_employee_aadhaar_employee_mothertounge_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='EmpSSN',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='leave',
            name='comment',
            field=models.TextField(null=True),
        ),
    ]
