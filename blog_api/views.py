from rest_framework import generics
from .serializers import PostSerializer
from .models import Post

class PostList(generics.ListCreateAPIView):
    queryset = Post.post_objects.all()
    serializer_class = PostSerializer
    pass

class PostDetail(generics.RetrieveDestroyAPIView):
    pass