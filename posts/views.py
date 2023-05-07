from rest_framework import generics, permissions
from django.core.mail import send_mail
from django.conf import settings
from .models import Post
from .serializers import PostSerializer
from .permissions import IsOwnerOrReadOnly

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        send_mail(
            'New Post Created',
            'A new post has been created!',
            settings.EMAIL_HOST_USER,
            [self.request.user.email],
            fail_silently=False,
        )

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user