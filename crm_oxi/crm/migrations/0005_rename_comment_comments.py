# Generated by Django 5.0.6 on 2024-06-25 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0004_rename_company_comment_record'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comment',
            new_name='Comments',
        ),
    ]
