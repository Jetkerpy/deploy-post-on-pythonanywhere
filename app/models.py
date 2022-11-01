from django.db import models

# Create your models here.



class Post(models.Model):
    name = models.CharField(max_length=200, verbose_name='Post ati', help_text='Post ushin ati kiritilsin.')
    image = models.ImageField(upload_to = 'post-images')

    def __str__(self):
        return self.name



        
