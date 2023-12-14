from django.db import models
from django.utils.translation import gettext_lazy as _

from common.base_models import BaseModel


class GeneratedImage(BaseModel):
    description = models.ForeignKey(to='descriptions.Description', verbose_name=_('description'),
                                    on_delete=models.PROTECT)
    image = models.ImageField(verbose_name=_('image'), upload_to='generated_images/%Y/%m/')
