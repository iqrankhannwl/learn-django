from django.db import models

# Create your models here.

class Blogs(models.Model):
    title =  models.CharField(max_length = 50)
    description = models.TextField()
    create_at = models.DateTimeField(auto_now_add = True)
    author = models.CharField(max_length = 20)
    tags = models.CharField(max_length = 50)