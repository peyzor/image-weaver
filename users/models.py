from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):

    def __str__(self):
        return f'{self.username}'

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
