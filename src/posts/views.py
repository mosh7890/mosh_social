from django.utils.translation import gettext as __
from rest_framework_extensions.mixins import NestedViewSetMixin
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import NotFound, PermissionDenied

from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer, LikeSerializer


class PostViewSet(NestedViewSetMixin, ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_destroy(self, instance):
        if self.request.user != instance.author:
            raise PermissionDenied(__('You do not have permission to delete this post.'))
        instance.delete()


class CommentViewSet(NestedViewSetMixin, ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_serializer_context(self):
        context = super(CommentViewSet, self).get_serializer_context()
        post_id = self.get_parents_query_dict().get('post')
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            raise NotFound(__(f'Post matching query id={post_id} does not exist.'))
        else:
            context.update({'post': post})
            return context

    def perform_destroy(self, instance):
        if self.request.user != instance.author:
            raise PermissionDenied(__('You do not have permission to delete this comment.'))
        instance.delete()


class LikeViewSet(NestedViewSetMixin, ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def get_serializer_context(self):
        context = super(LikeViewSet, self).get_serializer_context()
        post_id = self.get_parents_query_dict().get('post')
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            raise NotFound(__(f'Post matching query id={post_id} does not exist.'))
        else:
            context.update({'post': post})
            return context

    def perform_destroy(self, instance):
        if self.request.user != instance.author:
            raise PermissionDenied(__('You do not have permission to delete this like.'))
        instance.delete()
