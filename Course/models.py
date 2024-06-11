# from tkinter.tix import Tree
from django.db import models
from django.contrib.auth.models import User




class Type(models.Model):
    Name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100,unique=True, null=True, blank=True)

    def __str__(self):
        return self.Name
    

class AddCourse(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE,related_name='teacher' )
    Course_Title  = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=0 , null=True)
    Content = models.TextField()
    Type = models.ForeignKey(Type,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Course/media/uploads/', blank = True, null = True)

    def __str__ (self):
        return self.Course_Title

class Comment(models.Model):
    post = models.ForeignKey(AddCourse, on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=30)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Comments by {self.name}"

class EnrolledCourse(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    courses = models.ForeignKey(AddCourse,on_delete=models.CASCADE)

    def __str__(self):
        return f"buy this car name: {self.courses.Course_Title}"