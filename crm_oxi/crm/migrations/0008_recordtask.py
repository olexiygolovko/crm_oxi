# Generated by Django 5.0.6 on 2024-08-16 21:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0007_recordcomment_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecordTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('in_progress', 'In Progress'), ('completed', 'Completed'), ('overdue', 'Overdue')], default='in_progress', max_length=20)),
                ('due_date', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='redord_tasks', to='crm.record')),
            ],
        ),
    ]
