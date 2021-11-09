from django.db import models
from model_utils import Choices
from django.utils.translation import ugettext_lazy as _
from surveys.models import Poll


class Question(models.Model):
    """ Модель хранит вопросы для опросов. Каждый вопрос может быть связан только с одним опросом. """
    TYPE_QUESTION = Choices(
        (0, 'text', _('Текстовый ответ')),
        (1, 'select', _('Ответ с выбором одного варианта')),
        (2, 'multi_select', _('Ответ с выбором нескольких вариантов'))
    )

    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='quiz', verbose_name="Опрос")
    text = models.TextField(verbose_name="Текст вопроса")
    type = models.IntegerField(choices=TYPE_QUESTION, default=TYPE_QUESTION.text)

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"

    def __str__(self):
        return f"Вопрос № {self.pk} для опроса № {self.poll.pk}"


class Choice(models.Model):
    """ Модель хранить данные о выборках для вопросов """
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='election', verbose_name="Вопрос")
    name = models.CharField(max_length=255, verbose_name="Название выбора")

    class Meta:
        verbose_name = 'Выбор'
        verbose_name_plural = 'Выборы'

    def __str__(self):
        return self.name