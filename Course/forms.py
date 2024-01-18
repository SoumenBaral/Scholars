from django import forms
from . import models

class AddCourseFrom(forms.ModelForm):
    class Meta:
        model = models.AddCourse
        fields = ['Course_Title', 'Content', 'Type','price','image']

class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['name', 'email', 'body']