from rest_framework import generics
from rest_framework.permissions import BasePermission, SAFE_METHODS
from .serializers import PostSerializer
from .models import Post
from django.http import HttpResponse
# import requests

class PostBasePermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        message = 'Adding customers not allowed.'
        if request.method in SAFE_METHODS:
            return True
        else:
            return obj.author == request.user

class PostList(generics.ListAPIView):
    queryset = Post.post_objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [PostBasePermission]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    

# def rep(request):
#     url = "https://sandbox.repliers.io/listings?listings=true&operator=AND&sortBy=updatedOnDesc&status=A"
#     headers = {
#         "content-type": "application/json",
#         "REPLIERS-API-KEY": "I1H2jVeE6yKFRIWsoIqmH0Y8C2f5ON"
#     }
#     response = requests.get(url, headers=headers)
#     return HttpResponse(response.text)