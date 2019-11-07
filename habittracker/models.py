from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_registered = models.BooleanField(default=False)
    def __str__(self):
        return self.username

class Habit(models.Model):
    target = models.IntegerField()
    name = models.CharField(max_length=250)
    user = models.ForeignKey(
        to='User',
        on_delete=models.CASCADE,
        related_name='users',
        blank=True, 
        null=True,
    )
    created_at = models.DateField(default=timezone.now)
    updated_at = models.DateField(default=timezone.now)
    end_date = models.DateField(default=None, null=True)

    def __str__(self):
        return self.name

class Record(models.Model):
    record = models.TextField()
    habit = models.ForeignKey(
        to='Habit',
        on_delete=models.CASCADE,
        related_name='habits',
        blank=True, 
        null=True,
    )
    met_goal = models.BooleanField(default=False)
    created_at = models.DateField(default=timezone.now)
    updated_at = models.DateField(default=timezone.now)

    def __str__(self):
        return self.record

class Comment(models.Model):
    author = models.ForeignKey(to='User', on_delete=models.CASCADE, blank=True, null=True)
    habit = models.ForeignKey(to='Habit', on_delete=models.CASCADE, blank=True, null=True)
    comment = models.TextField()
    created_at = models.DateField(default=timezone.now)
    updated_at = models.DateField(default=timezone.now)

    def __str__(self):
        return self.comment
    

