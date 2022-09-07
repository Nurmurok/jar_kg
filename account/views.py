from django.http import Http404
from rest_framework import permissions, status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView

from blog.models import Post
from blog.serializers import PostSerializer
from .serializers import MyTokenObtainPairSerializer, UserSerializer
from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from .permissions import AnonPermissionOnly


class MyObtainPairView(TokenObtainPairView):
    permission_classes = (AnonPermissionOnly,)
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AnonPermissionOnly,)
    serializer_class = RegisterSerializer


class UserListApiView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        posts = User.objects.all()
        serializers = UserSerializer(posts, many=True)
        return Response(serializers.data)




class UserDetailApiView(APIView):
    permission_classes = [permissions.AllowAny]
    parser_classes = [JSONParser]

    def get_object(self, id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, id):
        user = self.get_object(id)
        posts = Post.objects.filter(user_id=id)
        serializer = UserSerializer(user)
        serializer2 = PostSerializer(posts, many=True)
        data = serializer.data
        data['posts'] = serializer2.data
        data['quantity_of_posts'] = posts.count()

        return Response(data)
