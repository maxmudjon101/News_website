from django.db import models
from django.utils import timezone
# Create your models here.
from django.contrib.auth.models import User


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=self.model.Status.Published)

    def __str__(self):
        return self.name


class Category(models.Model):
    name=models.CharField(max_length=250)

    def __str__(self):
        return self.name

class News(models.Model):

    class Status(models.TextChoices):
        Draft="DF","Draft"
        Published="PB","Published"

    title=models.CharField(max_length=250)
    slug=models.SlugField(max_length=250)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    image=models.ImageField(upload_to="news_image/")
    body=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    publish_time=models.DateTimeField(default=timezone.now)
    status=models.CharField(max_length=2,choices=Status.choices,default=Status.Draft)

    objects=models.Manager() #default
    published=PublishedManager() #ozgartirilgan

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-publish_time"]


class Comment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    new=models.ForeignKey(News,on_delete=models.CASCADE)
    body=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
