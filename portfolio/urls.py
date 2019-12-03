from django.urls import path
from . import views
from django.views.decorators.cache import never_cache   

app_name = 'portfolio'

urlpatterns = [
    path('', never_cache(views.home), name="home"),
    path('about/', never_cache(views.about), name="about-us"),
    path('contact/', never_cache(views.contact), name="contact"),
    path('categories/', never_cache(views.categories), name='categories'),


    path('projects', never_cache(views.project_list), name='project_list'),

    path('<slug:category_slug>/', never_cache(views.project_list), name='project_list_by_category'),
    path('<int:id>/<slug:slug>/', never_cache(views.project_detail), name='project_detail'),
]
