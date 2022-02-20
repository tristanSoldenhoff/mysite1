from django.urls import path
from . import views         #importing main_site/views.py

urlpatterns = [                             #path has 4 arguments: route, view, kwargs - optional, name - optional
    path('', views.index, name='index'),    #index is the def created in main_site/views.py
    path('<int:skill_id>/', views.detail, name='detail'),
    path('<int:skill_id>/results/', views.results, name='results'),
]
