from django.urls import path
from blog_app import views

app_name = 'blog_app'
urlpatterns = [
    path('', views.ListView.as_view(), name='post_list'),
    path('<int:pk>', views.DetailView.as_view(), name='detail'),
]
