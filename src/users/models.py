from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from stdimage.models import StdImageField


class User(AbstractUser):
    profile_pic = StdImageField(_('Profile Picture'),
                                help_text=_('Picture:JPG/JPEG.'),
                                upload_to='users/profile_pics',
                                variations={'thumbnail': (100, 100, True), },
                                blank=True,
                                null=True, )

    class Meta:
        db_table = 'users'
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return f'{self.username}'
