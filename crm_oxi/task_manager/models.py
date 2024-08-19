from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Task(models.Model):
    STATUS_CHOICES = [
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('overdue', 'Overdue'),
    ]
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='in_prograss')
    due_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Task {self.title} for {self.record}'

    def time_remaining(self):
        return self.due_date - timezone.now()

    def is_overdue(self):
        return timezone.now() > self.due_date
    
    
    