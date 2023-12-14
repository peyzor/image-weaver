from django.db import models
from django.utils.translation import gettext_lazy as _

from common.base_models import BaseModel


class Description(BaseModel):
    description = models.TextField(verbose_name=_('description'))
