from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from common.base_models import BaseModel

User = get_user_model()


class GeneratedImage(BaseModel):
    description = models.ForeignKey(to='descriptions.Description', verbose_name=_('description'),
                                    on_delete=models.PROTECT)
    image = models.ImageField(verbose_name=_('image'), upload_to='generated_images/%Y/%m/')


class UploadedImage(BaseModel):
    user = models.ForeignKey(to=User, verbose_name=_('user'), on_delete=models.PROTECT)
    image = models.ImageField(verbose_name=_('image'), upload_to='uploaded_images/%Y/%m/')
    description = models.TextField(verbose_name=_('description'), blank=True)

    def __str__(self):
        return f'{self.user.id} - {self.created_time}'
