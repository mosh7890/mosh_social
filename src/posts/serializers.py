import os
from django.utils.translation import gettext as __
from rest_framework.exceptions import APIException
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .models import Post, Comment, Like


class SimpleCommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'created_at', 'comment')


class SimpleLikeSerializer(ModelSerializer):
    class Meta:
        model = Like
        fields = ('id', 'author', 'post', 'created_at')


class PostSerializer(ModelSerializer):
    post_comments = SimpleCommentSerializer(many=True, read_only=True)
    post_likes = SimpleLikeSerializer(many=True, read_only=True)
    author_profile_pic_thumb = SerializerMethodField(read_only=True)
    image_thumb = SerializerMethodField(read_only=True)

    class Meta:
        model = Post

        fields = ('id', 'author', 'author_profile_pic_thumb', 'caption', 'image', 'image_thumb', 'created_at',
                  'post_comments', 'post_likes',)

        read_only_fields = ('id', 'author', 'created_at',)

    def create(self, validated_data):
        validated_data.update({'author': self.context.get('request').user})
        return super(PostSerializer, self).create(validated_data)

    @staticmethod
    def get_author_profile_pic_thumb(obj):
        if obj.author.profile_pic:
            name, ext = os.path.splitext(obj.author.profile_pic.url)
            return f'{name}.thumbnail{ext}'
        return

    @staticmethod
    def get_image_thumb(obj):
        if obj.image:
            name, ext = os.path.splitext(obj.image.url)
            return f'{name}.thumbnail{ext}'
        return


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'created_at', 'comment')
        read_only_fields = ('author', 'post', 'created_by',)

    def create(self, validated_data):
        validated_data.update({'author': self.context.get('request').user,
                               'post': self.context.get('post')})
        return super(CommentSerializer, self).create(validated_data)


class LikeSerializer(ModelSerializer):
    class Meta:
        model = Like
        fields = ('id', 'author', 'post', 'created_at')
        read_only_fields = ('author', 'post', 'created_at',)

    def validate(self, like):
        post = self.context.get('post')
        me = self.context.get('request').user
        if post.author == me:
            raise APIException(__('You may not like your own post.'))
        if post.post_likes.filter(author_id=me.id):
            raise APIException(__('You have already liked this post.'))
        return like

    def create(self, validated_data):
        validated_data.update({'author': self.context.get('request').user,
                               'post': self.context.get('post')})
        return super(LikeSerializer, self).create(validated_data)
