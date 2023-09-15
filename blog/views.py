from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView
from django.db.models import Q

from .forms import *
from .models import *
from .utils import DataMixin


class Bloglist(ListView):
    paginate_by = 5
    model = Post
    template_name = 'index.html'

    def get_queryset(self):
        queryset = Post.objects.all().order_by('-time')
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count'] = Post.objects.all().count()
        return context


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class SearchResultsView(ListView):
    paginate_by = 5
    model = Post
    template_name = 'index.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        queryset = Post.objects.filter(Q(author__username=query) | Q(title__icontains=query)).order_by('-time')
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count'] = Post.objects.all().count()
        context['q'] = self.request.GET.get('q')
        return context


class PoznavatelniyCategory(ListView):
    paginate_by = 5
    model = Post
    template_name = 'poznavatelniy.html'

    def get_queryset(self):
        queryset = Post.objects.filter(category=1).order_by('-time')
        return queryset


class LeniviyCategory(ListView):
    paginate_by = 5
    model = Post
    template_name = 'leniviy.html'

    def get_queryset(self):
        queryset = Post.objects.filter(category=2).order_by('-time')
        return queryset


class ChtotLenCategory(ListView):
    paginate_by = 5
    model = Post
    template_name = 'chtotonalenivom.html'

    def get_queryset(self):
        queryset = Post.objects.filter(category=3).order_by('-time')
        return queryset


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'register.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))


def logout_user(request):
    logout(request)
    return redirect('index')


class UserProfile(TemplateView):
    template_name = 'user_profile.html'
    model = User

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        urls_1 = []
        urls_1.append(self.request.path)
        urls_2 = []
        urls_3 = ''.join(urls_1)
        urls_2.append(urls_3[14:])
        context['users'] = User.objects.filter(id=int(urls_2[0]))
        return context


def addpage(request):
    if request.method == 'GET':
        form = AddPageForm(request.GET)
        if form.is_valid():
            try:
                Post.objects.create(**form.cleaned_data)
                return redirect('index')
            except:
                form.add_error(None, 'Ошибка добавления поста')
                return redirect('index')
    else:
        form = AddPageForm()
    return render(request, 'add_page.html', {'form': form})










