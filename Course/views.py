from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render,redirect
from . import models,forms
from django.views.generic import CreateView ,UpdateView,DeleteView,DetailView,ListView
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views import View

   
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_Mail(user,mail_subject,template):
        message= render_to_string(template, {
                "user": user,
                
            })
        send_email =EmailMultiAlternatives(mail_subject,"", to=[user.email])
        send_email.attach_alternative(message,'text/html')
        send_email.send()

@method_decorator(login_required, name= 'dispatch') 
class AddPostCreateView(CreateView):
    model = models.AddCourse
    form_class = forms.AddCourseFrom
    template_name = "addCourse.html"
    def get_success_url(self):
        return reverse_lazy('home')
    
    def form_valid(self, form):
        form.instance.teacher = self.request.user
        messages.success(self.request, 'Successfully Added a new Course sir. ')
        return super().form_valid(form)
    def form_invalid(self, form):
        response = super().form_invalid(form)
        messages.warning(self.request,"can't not create Post For this Course ")
        return response
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Create'
        return context




class UpdatePost(UpdateView):
    model = models.AddCourse
    form_class = forms.AddCourseFrom
    template_name = "addCourse.html"
    pk_url_kwarg='id'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Update'
        return context
    
    success_url = reverse_lazy('teacher')




def DeletePost(request,id):
    post = models.Posts.objects.get(pk=id)
    post.delete()
    return redirect('home')

class DeleteViewed(DeleteView):
        model = models.AddCourse
        template_name = "delete.html"
        pk_url_kwarg='id'
        success_url = reverse_lazy('teacher')


class DetailsPost(DetailView):
    model = models.AddCourse
    pk_url_kwarg = 'id'
    template_name = 'CourseDetails.html'

    def post(self,request,*args,**kwargs):
        comment_form = forms.CommentForm(data = self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit = False)
            new_comment.post = post 
            new_comment.save()
        return self.get(request, *args,**kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object
        comments = post.comments.all()
        comment_form = forms.CommentForm()
        
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context

class TeacherDashBoardView(View):
    
    template_name = 'TeacherDashboard.html'

    def get(self, request, category_slug=None):
        
        data = models.AddCourse.objects.filter(teacher=request.user)

        categories = models.Type.objects.all()

        if category_slug is not None:
            category = models.Type.objects.get(slug=category_slug)
            data = data.filter(Type=category)
        
        return render(request, self.template_name, {"data": data, "categories": categories})
 


class EnrolledCourseView(View):
     def get(self,request,id, **kwargs):
        courses = get_object_or_404(models.AddCourse, id = id)
        user = self.request.user
        models.EnrolledCourse.objects.create(
            courses = courses,
            user = user,
            date=datetime.now(),
        )
        send_Mail(self.request.user,'Successfully Enrolled','enroll_mail.html')
        messages.success(request, 'Enrolled  successful Please Review This Course so Another be inspired to Enrolled ')
        return redirect('home') 





class StudentView(LoginRequiredMixin, ListView):
    model = models.EnrolledCourse
    template_name = 'StudentDashboard.html'
    context_object_name = 'enrolled'

    def get_queryset(self):
        user_id = self.request.user.id
        queryset =  models.EnrolledCourse.objects.filter(user_id=user_id)
        return queryset