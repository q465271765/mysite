#coding=utf-8
from django.shortcuts import render
from blog.models import BlogsPost
from django.http import HttpResponse
from django.shortcuts import render_to_response

# Create your views here.


def index(request):
    blog_list = BlogsPost.objects.all()
    print(blog_list.count())
    #return HttpResponse(u"欢迎光临 自强学堂!")
    return render_to_response('index.html', {'blog_list': blog_list})
