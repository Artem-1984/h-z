from django.shortcuts import render,redirect
from django.views.generic.base import View
# Create your views here.
from .models import Post
from .form import CommentForm

class PostView(View):

    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'blog.html', context= {'post_list': posts})




class PostDetail(View):
    '''Отдельная страница'''
    def get(self,request, pk):
        post = Post.objects.get(id=pk)
        return render(request, 'blog_detail.html', {'post': post})

class AddComments(View):
    '''добавление комментов'''
    def post(self, request,pk):
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.post_id = pk
            form.save()
        return redirect(f'/{pk}')

