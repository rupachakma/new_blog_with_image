from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to="img",blank=True,null=True)
    file = models.FileField(upload_to="file")

def __str__(self):
    return self.title
