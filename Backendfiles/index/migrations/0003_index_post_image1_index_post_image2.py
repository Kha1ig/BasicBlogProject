# Generated by Django 4.0.3 on 2022-03-11 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_index_post_post_client_index_post_post_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='index_post',
            name='image1',
            field=models.ImageField(default='', upload_to='index_Post_detail/'),
        ),
        migrations.AddField(
            model_name='index_post',
            name='image2',
            field=models.ImageField(default='', upload_to='index_Post_detail/'),
        ),
    ]
