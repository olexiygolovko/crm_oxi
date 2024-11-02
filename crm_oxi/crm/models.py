from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    company_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    web_site = models.URLField(
        max_length=128, db_index=True, unique=True, blank=True, null=True
    )
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=20)

    def __str__(self):
        return(f"{self.first_name} {self.last_name}")


class RecordComment(models.Model):
    record = models.ForeignKey(Record, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Comment on {self.record.id} at {self.created_at}'
    

class RecordTask(models.Model):
    STATUS_CHOICES = [
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('overdue', 'Overdue'),
    ]

    record = models.ForeignKey(Record, related_name='redord_tasks', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='in_progress')
    due_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Task {self.title} for {self.record}'

    def time_remaining(self):
        return self.due_date - timezone.now()

    def is_overdue(self):
        return timezone.now() > self.due_date