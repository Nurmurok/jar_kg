from django.http import Http404
from django.shortcuts import render
from rest_framework.response import Response

from .models import Post
from rest_framework.views import APIView
from .serializers import PostSerializer
from rest_framework import permissions, status
from account.permissions import IsOwnerReadOnly




class PostListApiView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self,  request):
        posts = Post.objects.all()
        serializers = PostSerializer(posts, many=True)
        return Response(serializers.data)


class PostCreateApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        serializers = PostSerializer(data=request.data)
        if serializers.is_valid():
           serializers.save()
           return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetailApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get_object(self, id):
        try:
            return Post.objects.get(id=id)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, id):
        post = self.get_object(id)
        serializers = PostSerializer(post)
        data = serializers.data
        return Response(data)



class PostUpdateApiView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerReadOnly]

    def get_object(self, id):
        try:
            return Post.objects.get(id=id)
        except Post.DoesNotExist:
            raise Http404

    def put(self, requests,id):
        post = self.get_object(id)
        serializer = PostSerializer(post, data=requests.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDestroyApiView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerReadOnly]
    def get_object(self, id):
        try:
            return Post.objects.get(id=id)
        except Post.DoesNotExist:
            raise Http404

    def delete(self, requests, id):
        post = self.get_object(id)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


