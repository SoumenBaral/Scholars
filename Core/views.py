from typing import Type
from django.shortcuts import render
from django.views import View
from Course import models



class  HomeView(View):
    template_name = 'home.html'
    

    def get(self, request, category_slug=None):
        query = request.GET.get('q')
        data = models.AddCourse.objects.all()
        categories = models.Type.objects.all()
        if query:
            data = models.AddCourse.objects.filter(Course_Title__icontains=query)

        if category_slug is not None:
            category = models.Type.objects.get(slug=category_slug)
            data = models.AddCourse.objects.filter(Type=category)
        
        return render(request, self.template_name, {"data": data, "categories": categories})
    