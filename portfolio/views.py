from django.shortcuts import render, get_object_or_404
from .models import Category, Project


def home(request):
    project_1 = Project.objects.get(slug="sport-event")
    project_2 = Project.objects.get(slug="crypto-bank")
    project_3 = Project.objects.get(slug="online-shop")
    project_4 = Project.objects.get(slug="kaprekar-constant")
    return render(request, "home.html", {'project_1': project_1,
                                        'project_2': project_2,
                                        'project_3': project_3,
                                        'project_4': project_4})

def about(request):
    return render(request, "about.html", {})

def contact(request):
    return render(request, "contact.html", {})


def categories(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    projects = Project.objects.all()
    backend = Category.objects.get(slug="backend")
    frontend = Category.objects.get(slug="frontend")
    scraping = Category.objects.get(slug="scraping")
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        projects = projects.filter(category=category)
    return render(request, "portfolio/categories.html", 
                            {'category': category,
                            'categories': categories,
                            'projects': projects,
                            'backend': backend,
                            'frontend': frontend,
                            'scraping': scraping})


def project_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    backend = Category.objects.get(slug="backend")
    frontend = Category.objects.get(slug="frontend")
    scraping = Category.objects.get(slug="scraping")
    projects = Project.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        projects = projects.filter(category=category)
    return render(request, 
                    'portfolio/projects/list.html',
                    {'category': category,
                    'categories': categories,
                    'projects': projects, 'backend': backend, 'frontend': frontend, 'scraping': scraping})

def project_detail(request, id, slug):
    project = get_object_or_404(Project,
                                id=id,
                                slug=slug)
    return render(request,
                    'portfolio/projects/detail.html',
                    {'project': project})

    

