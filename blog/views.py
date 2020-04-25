from django.shortcuts import render, get_object_or_404
from .models import newProject

def all_blog(request):
    projects = newProject.objects.all()[:5]
    #projects = newProject.objects.order_by('-date')
    
    return render(request, 'blog/all_blog.html', {'projects':projects})

def detail(request, blog_id):
    blog = get_object_or_404(newProject, pk = blog_id)
    return render(request, 'blog/detail.html', {'blog':blog})
