from django import forms
from . import models

class AddCourseFrom(forms.ModelForm):
    class Meta:
        model = models.AddCourse
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['name', 'email', 'body']