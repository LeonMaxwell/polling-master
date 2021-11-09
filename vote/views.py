from django.http import Http404
from rest_framework import permissions, status, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from vote.models import Answer
from vote.serializers import AnswerSerializer


class CreateVote(generics.CreateAPIView):
    """ Данный класс предоставляет авторизированным пользователям отвечать на вопросы. """
    queryset = Answer
    serializer_class = AnswerSerializer
    permission_classes = [permissions.IsAuthenticated, ]
