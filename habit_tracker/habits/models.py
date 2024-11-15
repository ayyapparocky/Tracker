from django.db import models
from django.utils import timezone

class Habit(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Progress(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    completed = models.BooleanField(default=False)

    class Meta:
        unique_together = ('habit', 'date')  # Ensures only one progress entry per day per habit

    def __str__(self):
        return f"{self.habit.name} on {self.date}"
