# Generated by Django 4.0.3 on 2022-03-12 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_alter_contact_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='budget',
            field=models.CharField(choices=[('Budget Select', 'Budget Select'), ('$1200 to $1600', '-$1200 to $1600-'), ('$2200 to $2400', '-$2200 to $2400-'), ('$2500 to $3800', '-$2500 to $3800-')], default=(('Budget Select', 'Budget Select'), ('$1200 to $1600', '-$1200 to $1600-'), ('$2200 to $2400', '-$2200 to $2400-'), ('$2500 to $3800', '-$2500 to $3800-')), max_length=51),
        ),
    ]