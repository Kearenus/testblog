from django.shortcuts import render
from .models import Article
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import AddArticle, AuthUserForm, RegisterUserForm
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

class homepage(ListView):
    model = Article
    template_name = 'index.html'
    context_object_name = 'list_articles'

class SuccessMessage():
    @property
    def success_msg(self):
        return False
    def form_valid(self,form):
        messages.success(self.request, self.success_msg)
        return super().form_valid(form)
    def get_success_url(self):
        return '%s?id=%s' % (self.success_url, self.object.id)

class NewLogin(LoginView):
    template_name = 'login.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('edit_post')
    def get_success_url(self):
        return self.success_url

class NewRegistration(CreateView):
    model = User
    template_name = 'register_page.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('edit_post')
    success_msg = 'Вы успешно зарегистрированы!'

    def form_valid(self, form):
        form_valid = super().form_valid(form)
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        auth_user = authenticate(username=username, password=password)
        login(self.request, auth_user)
        return form_valid

class NewLogout(LogoutView):
    next_page = reverse_lazy('edit_post')


class post_number(DetailView):
    model = Article
    template_name = 'post.html'
    context_object_name = 'get_article'
    success_url = reverse_lazy('edit_post')

class edit_post(SuccessMessage, CreateView):
    model = Article
    template_name = 'edit_post.html'
    form_class = AddArticle
    success_url = reverse_lazy('edit_post')
    success_msg = 'Запись создана'
    def get_context_data(self,**kwargs):
        kwargs['list_articles'] = Article.objects.all().order_by('-id')
        return super().get_context_data(**kwargs)

class update_post(SuccessMessage, UpdateView):
    model = Article
    template_name = 'edit_post.html'
    form_class = AddArticle
    success_url = reverse_lazy('edit_post')
    success_msg = 'Запись обновлена'
    def get_context_data(self,**kwargs):
        kwargs['update'] = True
        return super().get_context_data(**kwargs)

class delete_post(DeleteView):
    model = Article
    template_name = 'edit_post.html'
    success_url = reverse_lazy('edit_post')
    success_msg = 'Запись удалена'
    def post(self, request, *args, **kwargs):
        messages.success(self.request, self.success_msg)
        return super().post(request)
