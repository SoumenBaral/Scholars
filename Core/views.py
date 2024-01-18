from typing import Type
from django.shortcuts import render
from django.views import View
from Course import models
from django.views.generic import TemplateView

# class(TemplateView):
#     template_name = 'home.html'
class  HomeView(View):
    template_name = 'home.html'

    def get(self, request, category_slug=None):
        data = models.AddCourse.objects.all()
        categories = models.Type.objects.all()

        if category_slug is not None:
            category = models.Type.objects.get(slug=category_slug)
            data = models.AddCourse.objects.filter(Type=category)
        
        return render(request, self.template_name, {"data": data, "categories": categories})
    