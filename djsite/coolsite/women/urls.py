from django.urls import path, re_path

from .views import *

urlpatterns = [
  
    path('', index, name='home'),                                         # прописали все маршруты текущего приложения  http://127.0.0.1:8000/
    path('about/', about, name='about'),
    path('add_page/', add_page, name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('<int:post_id>/', show_post, name='post'),
    path('category/<int:cat_id>/', show_category, name='category'),
] 

    