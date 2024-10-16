from django.db import models

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=50)
    image=models.ImageField(upload_to="Blog_images/",null=True,default=None)
    des=models.TextField()
    # pub_date=models.DateTimeField(auto_now_add=True)
    

        
    