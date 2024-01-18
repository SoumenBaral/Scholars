from django.shortcuts import render,redirect
from . import models,forms
from django.views.generic import CreateView ,UpdateView,DeleteView,DetailView
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

@method_decorator(login_required, name= 'dispatch') 
class AddPostCreateView(CreateView):
    model = models.AddCourse
    form_class = forms.AddCourseFrom
    template_name = "addCourse.html"
    def get_success_url(self):
        return reverse_lazy('home')
    
    def form_valid(self, form):
        form.instance.teacher = self.request.user
        messages.success(self.request, 'Successfully Added Car')
        return super().form_valid(form)
    def form_invalid(self, form):
        response = super().form_invalid(form)
        messages.warning(self.request,"can't not create Post For this Car ")
        return response

def EditPost(request,id):
    post = models.Posts.objects.get(pk=id)
    print(post.Name)
    if request.method == 'POST':
        form = forms.AddPost(request.POST ,instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = forms.AddPost(instance=post)
        return  render(request,'addCourse.html',{"form":form})


class UpdatePost(UpdateView):
    model = models.AddCourse
    form_class = forms.AddCourseFrom
    template_name = "addCourse.html"
    pk_url_kwarg='id'
    success_url = reverse_lazy('home')




def DeletePost(request,id):
    post = models.Posts.objects.get(pk=id)
    post.delete()
    return redirect('home')

class DeleteViewed(DeleteView):
        model = models.AddCourse
        template_name = "delete.html"
        pk_url_kwarg='id'
        success_url = reverse_lazy('profile')


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