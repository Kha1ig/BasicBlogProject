# Generated by Django 4.0.3 on 2022-03-22 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_alter_comment_date_add'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date_add',
            field=models.DateField(auto_now=True),
        ),
    ]
