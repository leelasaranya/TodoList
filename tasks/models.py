
# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    PRIORITY = (
        ('Low','Low'),
        ('Medium','Medium'),
        ('High','High'),
    )

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    priority = models.CharField(
        max_length=10,
        choices=PRIORITY,
        default="Medium"      # ✅ default value
    )
    due_date = models.DateField(
        null=True,
        blank=True            # ✅ optional
    )
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
