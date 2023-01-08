from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class meta:
        model = Post
        fields = ('id', 'title', 'author', 'excerpt', 'content', 'status')