#from django.shortcuts import render
# Create your views here.
from django.views.generic import TemplateView
from .models import Post
from django.views.generic import CreateView
from .forms import PostForm
from django.urls import reverse_lazy

class IndexView(TemplateView):
  template_name = "index.html"

  def get_context_data(self):
    context = super().get_context_data()
    context["posts"] = Post.objects.all().order_by('-created_at')
    return context

class PostCreateView(CreateView):
  model = Post
  template_name = "post.html"
  from_class = PostForm
  success_url = reverse_lazy('post:index')
  fields = "__all__"

  def form_valid(self, form):
    form.save()
    return super().form_valid(form)