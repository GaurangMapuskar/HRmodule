# Generated by Django 4.1.4 on 2023-01-15 05:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0019_alter_schedule_day'),
    ]

    operations = [
        migrations.RenameField(
            model_name='leave',
            old_name='comment',
            new_name='reason',
        ),
    ]