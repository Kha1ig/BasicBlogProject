# Generated by Django 4.0.3 on 2022-03-13 14:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_comment_blog_commenter'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='commenter',
            options={'ordering': ['name']},
        ),
    ]
