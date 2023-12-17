from django.db import models
from django.utils.translation import gettext_lazy as _

from common.base_models import BaseModel


class GIFOrder(BaseModel):
    title = models.CharField(verbose_name=_('title'), max_length=255)
    images = models.ManyToManyField(to='images.UploadedImage', verbose_name=_('images'), through='GIFOrderImage',
                                    related_name='gif_orders')

    def __str__(self):
        return f'{self.title}'


class GIFOrderImage(BaseModel):
    gif_order = models.ForeignKey(to='orders.GIFOrder', verbose_name=_('gif order'), on_delete=models.PROTECT)
    image = models.ForeignKey(to='images.UploadedImage', verbose_name=_('image'), on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.gif_order.id} - {self.image.id}'
