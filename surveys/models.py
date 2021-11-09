from datetime import datetime
from django.db import models

from django.contrib.auth.models import User


class Poll(models.Model):
    """ Модель хранящий созданные опросы в системе. Дату старта нельзя изменить после создании опроса."""
    name = models.CharField(max_length=255, verbose_name="Имя опроса")
    description = models.TextField(verbose_name="Описание опроса")
    created_at = models.DateTimeField(verbose_name="Дата начала опроса")
    finish_at = models.DateTimeField(verbose_name="Дата окончания опроса")

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'

    def __str__(self):
        return self.name
