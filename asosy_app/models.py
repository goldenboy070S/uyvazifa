from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(null=True)

    def __str__(self) -> str:
        return self.title
    