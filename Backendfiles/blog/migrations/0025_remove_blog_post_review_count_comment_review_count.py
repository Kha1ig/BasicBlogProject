# Generated by Django 4.0.3 on 2022-03-22 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_remove_comment_review_count_blog_post_review_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog_post',
            name='review_count',
        ),
        migrations.AddField(
            model_name='comment',
            name='review_count',
            field=models.IntegerField(default=0),
        ),
    ]
