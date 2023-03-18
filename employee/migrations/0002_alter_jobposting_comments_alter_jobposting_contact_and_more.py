# Generated by Django 4.1.4 on 2022-12-24 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobposting',
            name='comments',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='jobposting',
            name='contact',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='jobposting',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='jobposting',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='jobposting',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='jobposting',
            name='time',
            field=models.TimeField(auto_now_add=True),
        ),
    ]