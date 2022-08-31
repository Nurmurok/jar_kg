from django.shortcuts import render
from .models import Post
from .serializers import PostSerializer
from rest_framework import permissions, mixins, generics
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    UpdateAPIView,

)


class PostListApiView(ListAPIView):
    permission_classes = [permissions.AllowAny]
    # authentication_classes = []
    serializer_class = PostSerializer

    def get_queryset(self):
        qs = Post.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs


class PostCreateApiView(CreateAPIView):
    permission_classes = [permissions.AllowAny]
    # authentication_classes = []
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class PostDetailApiView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView ):

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)