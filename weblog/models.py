from django.db import models

def user_image_path(instance,filename):
    return 'user_{0}/%Y/%m/%d/{1}'.format(instance.author,filename)

# Create your models here.
class Post(models.Model):
    post_id=models.IntegerField()
    author=models.CharField(max_length=200)
    title=models.CharField(max_length=400)
    content=models.TextField()
    date=models.DateTimeField()
    image=models.ImageField(upload_to=user_image_path)

class Comment(models.Model):
    comment=models.TextField()
    commenter=models.CharField(max_length=200)
    email=models.EmailField()
    posts=models.ForeignKey(Post,on_delete=models.CASCADE) 