# Generated by Django 4.0.3 on 2022-03-13 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_comment_options_alter_comment_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='blog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='show_all_comments', to='blog.blog_post'),
        ),
        migrations.CreateModel(
            name='commenter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='show_commentters', to='blog.blog_post')),
            ],
        ),
    ]