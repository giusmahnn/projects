from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=500)
    title_tag = models.CharField(max_length=500, default="")
    author = models.CharField(max_length=100)
    body = models.TextField(max_length=10000000)
    date_created = models.DateField(auto_now_add=True)


    def __str__(self):
        return '{}:{}'.format(self.author, self.title)
    
    def get_absolute_url(self):
        #return reverse('post', args=(str(self.id)))
        return reverse('index')






class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.CharField(max_length=100)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return '{}:{}'.format(self.author, self.body)
    