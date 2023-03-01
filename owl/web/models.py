from django.db import models

# Create your models here.
class Monuments(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    description = models.TextField()

    def __str__(self) -> str:
        return self.name
