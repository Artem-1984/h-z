from django.shortcuts import render,redirect
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import BlodPost
from django.views.generic.base import View
from .form import BlogerForm,Add

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



class AddComments(View,PermissionRequiredMixin):

    def get(self,request):
        if not request.user.has_perm('bloger.add_blodpost'):
            raise PermissionDenied
        return render(request,'cm.html')

    def post(self,request):

        form1 = Add(request.POST)
        if form1.is_valid():
            form1 = form1.save(commit=False)
            form1.save()
        return HttpResponseRedirect('/')



