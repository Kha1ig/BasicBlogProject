# Generated by Django 4.0.3 on 2022-03-19 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_alter_comment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='status',
            field=models.CharField(choices=[('reject', 'Reject'), ('approve', 'Approve')], default=('reject', 'Reject'), max_length=50),
        ),
    ]
