from django.shortcuts import render,redirect
from django.template import loader
from django.http import HttpResponse
from .models import BlodPost
from django.views.generic.base import View
from .form import BlogerForm
# Create your views here.
class Blog(View):
    def get(self, request):
        posts = BlodPost.objects.all()

        return render(request, 'blog.html', {'posts': posts})


class PostBlog(View):
    """Отображения отдельной статьи блога """
    def get(self,request,pk):
        post = BlodPost.objects.get(id=pk)
        return render(request,'post.html',{'post':post})


class AddComment(View):
    def post(self,request,pk):
        form = BlogerForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.post_id = pk
            form.save()
        return redirect(f'/{pk}')
