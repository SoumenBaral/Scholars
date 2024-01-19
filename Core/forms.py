# forms.py
from django import forms
from .models import Message

class MessageModelForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'email', 'content']