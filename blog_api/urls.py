from django.urls import path
from . import views     

app_name = 'blog_api'

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<int:pk>/', views.PostDetail.as_view(), name='blog'),
]