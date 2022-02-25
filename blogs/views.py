from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse

def root(request):
    return redirect("/blogs")

def index(request):
    return HttpResponse("placeholder to display a list of all blogs")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    return redirect("/")

def show(request, blog_id):
    number = blog_id
    html = 'placeholder to display blog number: {}'.format(number)
    return HttpResponse(html)

def edit(request, blog_id):
    number = blog_id
    html = 'placeholder to edit blog number: {}'.format(number)
    return HttpResponse(html)

def destroy(request, blog_id):
    return redirect("/blogs")

def jason(request):
    return JsonResponse({"title": "My first blog", "content":"I made my first blog!"})

# Create your views here.
