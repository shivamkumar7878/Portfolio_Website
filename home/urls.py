from django.urls import path
from . import views
urlpatterns = [
    
    path('', views.home_view, name='Home'),
    path("download/", views.download_cv, name="download_cv"),
    path('About/' ,views.about_view ,name='about'),
     path('contact/', views.contact_view, name='contact'),
    path('send', views.send_view, name='send'),
    path('work',views.work_view,name="work"),
    path('skill',views.skill_view,name="skill"),

]