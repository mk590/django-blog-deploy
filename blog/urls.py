from django.urls import path

from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('form-blog/',views.form,name='form'),
    path('blog-del/<int:pk>/',views.specific_blog_del,name='specific_blog_del'),
    path('blog-update/<int:pk>/',views.specific_blog_update,name='specific_blog_update'),
    path('blog-view/<int:pk>/',views.specific_blog_view,name='specific_blog_view'),
      path('favicon.ico/', views.favicon),
]
