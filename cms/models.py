from django.db import models
from ckeditor.fields import RichTextField


class Post(models.Model):
    title = models.CharField(max_length=120)
    content = RichTextField()
    image = models.ImageField(upload_to='uploads/')
    status = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return self.title.title()


class Gallery(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='uploads/')
    status = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return self.name if self.name else self.image.url

