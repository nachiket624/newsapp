# Generated by Django 4.2.4 on 2023-08-26 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('siteadmin', '0003_category_item_alter_news_youtube_alter_news_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='cat',
            new_name='category',
        ),
    ]
