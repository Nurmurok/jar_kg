from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    # image_url = serializers.SerializerMethodField('get_image_url')
    class Meta:
        model = Post
        fields = ['id', 'user', 'title', 'content', 'image']






