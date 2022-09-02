from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.filters import PostFilter
from blog.forms import CretePostForm
from blog.models import Post


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'post'
    ordering = ['-date_posted']  # newest to oldest
    # ordering=['date_posted'] #oldest to newest
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context
    # class PostFilter(django_filters.FilterSet):
    #     title = django_filters.CharFilter(lookup_expr='icontains')

    #     class Meta:
    #         model = Post
    #         fields = ['title', 'author']


class UserPostListView(ListView):
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    # creating a post #without login required without login also one can go to that page,
    # but we need to redirect them at login page so
    # don't interchange (login,create) argument
    model = Post
    # url = object.get_absolute_url('post-detail')
    # fields = ['title', 'content']
    form_class = CretePostForm

    # to inform django that author is currently logged-in user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    # post is created, but it doesn't know where to redirect after creating post so need to change in
    # blog/models.py


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    # creating a post 
    # without login required without login also one can go to that page
    # using UserPassesTestMixin who wrote a blog is only able to update it,
    # but we need to redirect them at login page so
    # don't interchange (login,create) argument
    model = Post
    fields = ['title', 'content']

    # to inform django that author is currently logged-in user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # add in url

    # check logged-in user==author of post
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post

    def get_success_url(self):
        return reverse('blog-home')

    # success_url='/'
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


def about(request):
    return render(request, 'blog/about.html', {'title': 'about'})
