"""blog_project URL Configuration

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
from django.urls import path,include

# to include image 
from django.conf import settings
from django.conf.urls.static import static

# to include users 
from users import views as user_views
    # is it imported as user_views to avoid confusion 
    
# for the login/logout/authentication
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',include('blog.urls')),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    # path('login/',auth_views.LoginView.as_view(template_name='blog/Templates/login.html'),name='login'),
    path('login/',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='logout.html'),name='logout'),
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



# path('login/',auth_views.LoginView.as_view(),name='login'),
# the error displayed 
# TemplateDoesNotExist at /login/
# registration/login.html 

# registration/login.html --> this is the by deafult place for django to look for the templates 

# as_view(template_name='path of the file ')
# path('login/',auth_views.LoginView.as_view(template_name='blog/Templates/login.html'name='login'),
# error 
# C:\SDE\blog_project\blog\templates\blog\Templates\login.html (Source does not exist)
# we need to pass the path only as the login.html as it is by default looking at that directory 