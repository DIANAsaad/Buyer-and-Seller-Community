# Generated by Django 5.0.7 on 2024-10-03 17:59

import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_post_price_alter_post_author_like'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='like',
            old_name='author',
            new_name='liker',
        ),
        migrations.AlterUniqueTogether(
            name='like',
            unique_together={('post', 'liker')},
        ),
        migrations.AddField(
            model_name='like',
            name='liked_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.RemoveField(
            model_name='like',
            name='like_count',
        ),
    ]