from django.contrib.auth import get_user_model
from django.contrib.humanize.templatetags.humanize import naturaltime
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from stdimage.models import StdImageField


class Post(models.Model):
    author = models.ForeignKey(get_user_model(),
                               verbose_name=_('Author'),
                               help_text=_('Uploader'),
                               related_name='user_posts',
                               on_delete=models.SET_NULL,
                               null=True)
    image = StdImageField(_('Image'),
                          help_text=_('Picture:JPG/JPEG'),
                          upload_to='posts/images',
                          variations={
                              'thumbnail': (100, 100, True), })
    caption = models.CharField(_('Caption'),
                               help_text=_('Caption/Description'),
                               max_length=255,
                               default='')
    created_at = models.DateTimeField(_('Created At'),
                                      help_text=_('Date/Time.'),
                                      auto_now_add=True)

    class Meta:
        db_table = 'posts'
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')
        ordering = ('created_at',)

    def __str__(self):
        return f'{self.author}: {naturaltime(timezone.localtime(self.created_at))}'


class Comment(models.Model):
    author = models.ForeignKey(get_user_model(),
                               verbose_name=_('Author'),
                               help_text=_('Author'),
                               related_name='user_comments',
                               on_delete=models.SET_NULL,
                               null=True)
    post = models.ForeignKey(Post,
                             verbose_name=_('Post'),
                             help_text=_('Post'),
                             related_name='post_comments',
                             on_delete=models.SET_NULL,
                             null=True)
    comment = models.CharField(_('Comment'),
                               help_text=_('Comment'),
                               max_length=255)
    created_at = models.DateTimeField(_('Created At'),
                                      help_text=_('Date/Time.'),
                                      auto_now_add=True)

    class Meta:
        db_table = 'comments'
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')
        ordering = ('created_at',)

    def __str__(self):
        return f'{self.author}: on post with ID# {self.post_id} {naturaltime(timezone.localtime(self.created_at))}'


class Like(models.Model):
    author = models.ForeignKey(get_user_model(),
                               verbose_name=_('Author'),
                               help_text=_('Author'),
                               related_name='user_likes',
                               on_delete=models.SET_NULL,
                               null=True)
    post = models.ForeignKey(Post,
                             verbose_name=_('Post'),
                             help_text=_('Post'),
                             related_name='post_likes',
                             on_delete=models.SET_NULL,
                             null=True)
    created_at = models.DateTimeField(_('Created At'),
                                      help_text=_('Date/Time.'),
                                      auto_now_add=True)

    class Meta:
        db_table = 'likes'
        verbose_name = _('Like')
        verbose_name_plural = _('Likes')
        ordering = ('created_at',)
        unique_together = ('author', 'post')

    def __str__(self):
        return f'{self.author}: on post with ID# {self.post} {naturaltime(timezone.localtime(self.created_at))}'
