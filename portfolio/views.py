from django.shortcuts import render, get_object_or_404
from .models import Category, Project, Img
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
from django.contrib import messages

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
    diving = Img.objects.get(slug="diving")
    voyager = Img.objects.get(slug="voyager")
    return render(request, "about.html", {'diving': diving,
                                        'voyager': voyager})

def contact(request):
    if request.method == 'POST':
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message_phone = request.POST['message-phone']
        message = request.POST['message']

        if message_phone:
            message += "\n\n" + message_email + "\n" + message_phone
        else:
            message += "\n\n" + message_email

        send_mail(message_name,message,'kubousky@gmail.com',['jakub.parcheta@gmail.com'],fail_silently=False)
        # messages.success(request, ('Thank you %s! We received your email and will contact you shortly.' % message_name))
        messages.success(request, (message_name))
        return render(request, "contact.html", {})
    else:
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

    # si quiera quitar paginas hay que volver a cambier '{% for project in page_projects %}' en list.html por '{% for project in projects %}'
    paginator = Paginator(projects, 8)
    page = request.GET.get('page')
    page_projects = paginator.get_page(page)

    return render(request, 
                    'portfolio/projects/list.html',
                    {'category': category,
                    'categories': categories,
                    'projects': projects, 
                    'backend': backend, 
                    'frontend': frontend, 
                    'scraping': scraping,
                    'page_projects': page_projects})


def project_detail(request, id, slug):

    projects = Project.objects.order_by('pk')
    paginator = Paginator(projects, 1)
    if 'page' in request.GET:
        project = paginator.get_page(request.GET['page'])
    else:
        page = Project.objects.filter(pk__lte=id).count()
        project = paginator.get_page(page)
    
    return render(request,
                    'portfolio/projects/detail.html',
                    {'project': project})





    

