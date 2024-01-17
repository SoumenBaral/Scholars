from django.db import models
from django.contrib.auth.models import User


class Type(models.Model):
    Name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100,unique=True, null=True, blank=True)

    def __str__(self):
        return self.Name





class AddCourse(models.Model):
    Name  = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=0 , default=0.00)
    quantity = models.IntegerField(default=0)
    Content = models.TextField()
    brand = models.ForeignKey(Type,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='carModel/media/uploads/', blank = True, null = True)

    def __str__ (self):
        return self.Name

class Comment(models.Model):
    post = models.ForeignKey(AddCourse, on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=30)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Comments by {self.name}"

class BuyCar(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    car = models.ForeignKey(AddCourse,on_delete=models.CASCADE)

    def __str__(self):
        return f"buy this car name: {self.car.Name}"