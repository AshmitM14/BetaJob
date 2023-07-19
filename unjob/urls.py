"""unjob URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from betajob import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index ),
    path('about/', views.about),
    path('contact/', views.contact),
    path('signup/', views.handleSignUp),
    path('login/', views.handleLogin),
    path('logout/', views.handleLogout),
    path('jobs/', views.findjobs),
    path('post-jobs/', views.postJobs),
    path('post/', views.JobPostHandle),
    path('contactHandle/', views.ContactHandle),
    path('dashboard/', views.dashboard),
    path('search/', views.search),

]