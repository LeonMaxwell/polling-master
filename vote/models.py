from django.contrib.auth.models import User
from django.db import models

from questions.models import Question


class Answer(models.Model):
    """ Модель которая хранит ответы на вопросы. """
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answer', verbose_name="Вопрос")
    text = models.TextField(verbose_name="Ответ")

    class Meta:
        verbose_name = "Ответ на вопрос"
        verbose_name_plural = "Ответы на вопрос"

    def __str__(self):
        return f"Ответ {self.user.pk} на вопрос {self.question.pk}"
