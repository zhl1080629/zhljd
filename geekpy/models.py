from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=20)
    author = models.CharField(max_length=10)
    content = models.CharField(max_length=1024)

    class Meta():
        db_table = 'article'
