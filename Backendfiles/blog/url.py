from django.urls import path
from blog.views import blog, blog_detail

app_name = 'blog'

urlpatterns = [
    
    path('', blog, name = 'blog' ),
    path('<int:pk>', blog_detail, name = 'blog-detail'),
   


]