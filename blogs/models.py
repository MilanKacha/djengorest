from django.db import models

# Create your models here.

# nested modal
class Blogs(models.Model):
    blog_title = models.CharField(max_length=100)
    blog_body = models.TextField()
    
    def __str__(self):
        return self.blog_title
    
    class Meta:
        verbose_name_plural = "Blogs"
    
    
class Comment(models.Model):
    blog = models.ForeignKey(Blogs, on_delete=models.CASCADE, related_name='comments')  # blog delete then Comment automatically delete
    
    comment = models.TextField()
    
    def __str__(self):
        return self.comment