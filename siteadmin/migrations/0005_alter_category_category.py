# Generated by Django 4.2.4 on 2023-08-31 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteadmin', '0004_rename_cat_category_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(max_length=60, unique=True),
        ),
    ]
