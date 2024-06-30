from django.db import models


class Baner(models.Model):
    title = models.CharField(max_length=255)
    detail = models.TextField()
    background_img = models.ImageField(upload_to="media/", verbose_name="Background Image")
    
    
    def __str__(self):
        return self.title


class Service(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(upload_to="media/", verbose_name="Image")
    image = models.ImageField(default='default_image.png')


class Contact(models.Model):
    f_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 13)
    text = models.TextField()
    is_watch = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.f_name}"
    

class Info(models.Model):
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    email = models.EmailField()

    def __str__(self):
        return self.phone
