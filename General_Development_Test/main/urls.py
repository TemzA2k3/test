from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('aboutproject/', views.about_project, name='aboutproject'),
    path('questions/<int:question_id>', views.question, name='question'),
    path('results/', views.results, name='res'),
    path('rules/', views.rules, name='rules'),

]
