from django.db import models


# Create your models here.

class ExampleModel(models.Model):
    name = models.CharField(max_length=100)


class Post(models.Model):
    objects = None
    title = models.CharField(max_length=100)
    content = models.TextField()
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
