from django.urls import path
from .views import PostListApiView,PostCreateApiView,PostDetailApiView

urlpatterns = [
    path('list/', PostListApiView.as_view(), name='list'),
    path('create/', PostCreateApiView.as_view(), name='create'),
    path('detail/<int:pk>/', PostDetailApiView.as_view(), name='detail'),

]
