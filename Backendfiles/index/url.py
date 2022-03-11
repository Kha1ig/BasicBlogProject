from django.urls import path
from index.views import index, index_detail

app_name = 'index'

urlpatterns = [
    path('', index, name='index'),
    path('<int:pk>', index_detail, name='index_detail'),

]