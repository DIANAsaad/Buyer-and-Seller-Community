# Generated by Django 5.0.7 on 2024-10-08 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_remove_profile_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
    ]