# Generated by Django 4.0.3 on 2022-03-12 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0006_alter_about_work_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about_work',
            name='work_subtitle_4',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
    ]
