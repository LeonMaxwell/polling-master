from collections import namedtuple

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status, generics

from questions.models import Question
from vote.models import Answer
from .models import Poll
from .serializers import PollSerializer, PassedPollSerializer


class ListPoll(APIView):
    """ Данный класс показывает данные опроса которые в данный момент активны,
    но только авторизированным пользователям."""
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        poll_active = PollSerializer(Poll.objects.filter(finish_at__gte=timezone.now()), many=True)
        if not poll_active.data:
            return Response("Нет активных опросов", status.HTTP_404_NOT_FOUND)
        return Response(poll_active.data, status.HTTP_200_OK)


class CreatePoll(generics.CreateAPIView):
    """ Данный класс предоставляет авторизированным пользователям создать свой опрос. """
    queryset = Poll
    serializer_class = PollSerializer
    permission_classes = [permissions.IsAuthenticated, ]


class PollDetail(APIView):
    """ Класс предоставляет более подробную информацию об опросе, так же с возможностью его редактировать и удалить.
     Доступно только авторизированным пользователям."""
    serializer_class = PollSerializer
    permission_classes = (permissions.IsAuthenticated,)

    @staticmethod
    def get_object(pk):
        try:
            return Poll.objects.get(pk=pk)
        except Poll.DoesNotExist:
            raise Http404

    def get(self, request, pk, *args, **kwargs):
        poll = self.get_object(pk=pk)
        serializer = PollSerializer(poll)
        return Response(serializer.data)

    def put(self, request, pk, *args, **kwargs):
        poll = self.get_object(pk=pk)
        serializer = PollSerializer(poll, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        poll = self.get_object(pk=pk)
        poll.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ListPassedPoll(APIView):
    """ Данный класс представляет полную информацию об пройденных опросах пользователя. В представление входит
    как и сами вопросы которые включены в опрос, так и их ответ на эти вопросы указанного пользователя. """
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, user_pk, *args, **kwargs):
        poll = Poll.objects.filter(quiz__answer__user_id=user_pk).distinct().all()
        poll_passed = PassedPollSerializer(poll, many=True)
        if not poll_passed.data:
            return Response("Нет пройденных опросов", status.HTTP_404_NOT_FOUND)
        return Response(poll_passed.data, status.HTTP_200_OK)