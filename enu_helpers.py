from django.utils.translation import gettext_lazy as _
from django.db import models

class CategoryChoices(models.TextChoices):
    LOW = 'low', _('Low')
    MEDIUM = 'medium', _('Medium')
    HIGH = 'high', _('High')