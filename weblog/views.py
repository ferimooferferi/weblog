from django.shortcuts import render,get_object_or_404
from django.views.generic import *
from .models import *
from .forms import *
from django.db.models import Count
from django.http import HttpResponseRedirect,Http404,HttpResponse
from django.urls import reverse,reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.mail import BadHeaderError,send_mail,mail_admins
from django.core.paginator import Paginator
from datetime import datetime

# Create your views here.
class HomeView(ListView):
    template_name='index.html'
    context_object_name='comment_list'

    def get_context_data(self,**kwargs):
        context=super(ListView,self).get_context_data(**kwargs)
        context['post_list']=Post.objects.all().reverse()
        return context  

    def get_queryset(self,**kwargs):
        pass

class PageView(ListView):
    template_name='page.html'

    def get_context_data(self,**kwargs):
        context=super(ListView,self).get_context_data(**kwargs)
        post_list=Post.objects.all().reverse()
        paginator=Paginator(post_list,5)

        page=self.request.GET.get('pagenr')

        posts=paginator.get_page(page)
        context['post_page_list']=posts
        return context

    def get_queryset(self,**kwargs):
        pass    

class PostView(ListView):
    template_name='blog.html'
    context_object_name='post_list'

    def get_context_data(self,**kwargs):
        context=super(ListView,self).get_context_data(**kwargs)
        context['post']=Post.objects.get(post_id=self.kwargs['pagenr'])
        context['comment_list']=Comment.objects.all()
        return context

    def get_queryset(self,**kwargs):
        pass 

@method_decorator(login_required,name='dispatch')
class AddPostView(TemplateView):
    template_name='createPost.html'

    def post(self,request,*args,**kwargs):  
        date=datetime.now()
        author=request.POST.get('author')
        title=request.POST.get('title')
        content=request.POST.get('content')
        image=request.FILES['image']
        post=Post(
            post_id=Post.objects.all().count()+1,
            author=author,
            title=title,
            content=content,
            date=date,
            image=image
        )
        post.save()
        return HttpResponseRedirect(reverse('home'))  

class DeletePostView(DeleteView):
    model=Post
    success_url=reverse_lazy('home')
    template_name='post_confirm_delete.html'

class ContactView(ListView):
    template_name='contact.html'
    model=Post
    context_object_name='post_list'

class AboutView(ListView):
    template_name='about.html'
    context_object_name='comment_list'

    def get_queryset(self):
        return Comment.objects.all()

    def get_context_data(self,**kwargs):
        context=super(ListView,self).get_context_data(**kwargs)
        context['post_list']=Post.objects.all()
        return context   

class CommentView(View):
    def post(self,request,*args,**kwargs):
        post_id=self.kwargs['post_id']
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')

        posted=get_object_or_404(Post,post_id=post_id)
        comment=Comment(comment=message,commenter=name,email=email,posts=posted)
        comment.save()
        return HttpResponseRedirect(reverse('post',args=(post_id,))) 

class SearchView(View):
    def get(self,request,*args,**kwargs):
        pass

class SendEmailView(View):
    def post(self,request,*args,**kwargs):
        subject='Reply from blog visitor.'
        message=request.POST.get('message','')
        from_email=request.POST.get('email','')
        if message and from_email:
            try:
                #send_mail(subject,message,from_email,['fuckshit@cliptik.net'])
                mail_admins(subject,message)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponseRedirect(reverse('contact'))
        else:
            return HttpResponse('Please Enter all fields correctly.')        