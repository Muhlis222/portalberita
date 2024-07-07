from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, editable=False)
    author = models.CharField(max_length=100)
    deskripsi = models.TextField()
    body = models.TextField()
    keyword = models.TextField()
    status = models.CharField(max_length=100, choices=(('1', 'publish'), ('2', 'unpublish')))
    create_date = models.DateTimeField(default=timezone.now, editable=False)
    publish_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    # def save(self):
    #     self.slug = slugify(self.title)
    #     super(Post, self).save()

    # def get_absolute_url(self):
    #     return '/%s/' % self.slug

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    message = models.TextField()
    date_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name