from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='category_images/', blank=True, null=True)

    def __str__(self):
        return self.name

class Omonim(models.Model):
    word = models.CharField(max_length=100)
    meanings = models.TextField()  # JSON yoki \n bilan ajratilgan matnlar
    example = models.TextField(blank=True, null=True)
    audio = models.FileField(upload_to='audio/', blank=True, null=True)
    categories = models.ManyToManyField(Category, related_name='omonims')

    def __str__(self):
        return self.word
