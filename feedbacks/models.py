from django.db import models
from enum import Enum

# Create your models here.
class FeedbackType(Enum):
    COMPLAINT = 1
    PRAISE = 2
    SUGESTION = 3

class Feedback(models.Model):
    type = models.IntegerField(choices=[(type.value, type.name) for type in FeedbackType])
    content = models.TextField(max_length=200)
    client_name = models.CharField(max_length=20, default="")
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.get_type_display()} - {self.creation_date}"