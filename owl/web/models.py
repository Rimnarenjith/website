from django.db import models
from django.utils.text import slugify

# Create your models here.
class Monuments(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    slug = models.SlugField(unique=True, max_length=100)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name
    
    def save(self, *args, **kwargs):
        # Auto-generate slug from name field
        self.slug = slugify(self.name)
        super(Monuments, self).save(*args, **kwargs)

