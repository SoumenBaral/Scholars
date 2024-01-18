from django.shortcuts import render,redirect
from . import forms
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import CreateView,UpdateView,DeleteView,View
from django.contrib.auth.forms import AuthenticationForm ,PasswordChangeForm
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.views import LoginView, LogoutView,PasswordChangeView
from django.contrib.auth.decorators import login_required 
from django.utils.decorators import method_decorator
from django.contrib.auth import login,logout
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
import binascii


from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


class RegistrationFormView(CreateView):
    template_name = 'register.html'
    form_class = forms.RegistrationForm
    success_url = reverse_lazy('accounts:login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        messages.success(self.request, 'Please Check your Account and Active Your Account')
        current_site = get_current_site(self.request)
        subject = 'Activate Your Account'
        message = render_to_string('account_activation_email.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': default_token_generator.make_token(user),
        })
        to_email = form.cleaned_data.get('email')
        email = EmailMultiAlternatives(subject, message, to=[to_email])
        email.send()

        return super().form_valid(form)
       
    def form_invalid(self, form):
        response = super().form_invalid(form)
        messages.warning(self.request, 'SignUp in information incorrect')
        return response
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Register'
        return context


def activate_account(request, uidb64, token):
    print(uidb64)
    users = User.objects.get(pk=uidb64)
    users.is_active = True
    users.save()
    return render(request, 'account_activation_success.html')

class UserLoginView(LoginView):
    template_name ='register.html'

    def get_success_url(self):
        return reverse_lazy('home')
    
    def form_valid(self, form):
        messages.success(self.request, 'Logged in Successfully')
        return super().form_valid(form)
    
    
    def form_invalid(self, form: AuthenticationForm) -> HttpResponse:
        messages.warning(self.request, 'Logged in information incorrect')
        return super().form_invalid(form)
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context
    

def logOut(request):
    logout(request)
    messages.success(request, "You have been successfully logged out.")
    return redirect('accounts:login')