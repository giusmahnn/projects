from django.urls import path
from .views import AddPostView,UpdatePostView,DeletePostView
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('post/<str:pk>/', views.post, name='post'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('post/edit/<str:pk>', UpdatePostView.as_view(), name='update_post'),
    path('post/<str:pk>/delete/', DeletePostView.as_view(), name='delete_post'),
]
