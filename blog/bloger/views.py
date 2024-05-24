from django.shortcuts import render,redirect
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import BlodPost,Blogers
from django.views.generic.base import View
from .form import BlogerForm,Add,Replacement
from users.forms import LoginUserForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.
class Blog(View):
    def get(self, request):
        posts = BlodPost.objects.all()
        a = BlodPost.objects.all()
        print(a)
        return render(request, 'blog.html', {'posts': posts})



class PostBlog(View,PermissionRequiredMixin):



    """Отображения отдельной статьи блога """
    def get(self,request,pk):
        if not request.user.has_perm('bloger.add_blogers'):
            raise PermissionDenied
        else:
            post = BlodPost.objects.get(id=pk)
            return render(request,'post.html',{'post':post})
    # def get(self,request,pk):
    #     post = Blogers.objects.get(id=pk)
    #     return render(request, 'red.html', {'post': post})
    # def post(self,request,pk):
    #
    #     person = Blogers.objects.get()
    #     person.delete()
    #
    #     return redirect(f'/{pk}')


class AddComment(View,PermissionRequiredMixin):

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

class Ser(View):
    def get(self,request):

        return render(request,'a.html')

    def post(self,request):
        request.user.groups.add(8)
        request.user.user_permissions.add(29)
        return HttpResponseRedirect('/')

class Red(View):
    def get(self,request,pk):
        if not request.user.has_perm('bloger.change_blogers') and not request.user.has_perm('bloger.delete_blogers'):
            raise PermissionDenied
        else:
            post = Blogers.objects.get(id=pk)
            return render(request, 'red.html', {'post': post})
class Rep(View):
    def post(self,request,pk):
        form = Replacement(request.POST)
        print(form)
        num = Blogers.objects.filter(id=pk).update(text=form.cleaned_data['text'])
        return HttpResponseRedirect('/')
class Del(View):
    def post(self,request,pk):
        form = Blogers.objects.get(id = pk)
        form.delete()
        return HttpResponseRedirect('/')