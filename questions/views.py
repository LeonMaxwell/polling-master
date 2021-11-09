from django.http import Http404
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import QuestionSerializer, ChoiceSerializer
from questions.models import Question, Choice


class CreateQuestion(generics.CreateAPIView):
    """ Данный класс предоставляет авторизированным пользователям создать свой вопрос. """
    queryset = Question
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated, ]


class QuestionDetail(APIView):
    """ Класс предоставляет более подробную информацию о вопросе, так же с возможностью его редактировать и удалить.
     Доступно только авторизированным пользователям."""
    serializer_class = QuestionSerializer
    permission_classes = (permissions.IsAuthenticated,)

    @staticmethod
    def get_object(pk):
        try:
            return Question.objects.get(pk=pk)
        except Question.DoesNotExist:
            raise Http404

    def get(self, request, pk, *args, **kwargs):
        question = self.get_object(pk=pk)
        serializer = QuestionSerializer(question)
        return Response(serializer.data)

    def put(self, request, pk, *args, **kwargs):
        question = self.get_object(pk=pk)
        serializer = QuestionSerializer(question, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        question = self.get_object(pk=pk)
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ChoiceView(APIView):
    """ Класс который представляет возможность создавать выборки для вопросов. Только если позволяет тип вопроса. """
    serializer_class = ChoiceSerializer
    permission_classes = (permissions.IsAuthenticated,)

    @staticmethod
    def get_object(pk):
        try:
            return Choice.objects.filter(question_id=pk)
        except Choice.DoesNotExist:
            raise Http404

    def get(self, request, pk, *args, **kwargs):
        question = Question.objects.get(pk=pk)
        if question.type == 0:
            return Response("У данного вопроса не предусмотрено выбирать ответ. ")
        else:
            choice = self.get_object(pk=pk)
            serializer = ChoiceSerializer(choice, many=True)
            return Response(serializer.data)

    def post(self, request, pk, *args, **kwargs):
        questions = Question.objects.get(pk=pk)
        if questions.type == 0:
            return Response("У данного вопроса не предусмотрено выбирать ответ. ")
        else:
            choice = Choice()
            choice.question = questions
            choice.name = request.data['name']
            choice.save()
            choice = self.get_object(pk=pk)
            serializer = ChoiceSerializer(choice, many=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class ChoiceDetail(APIView):
    """ Класс представляет информацию о выборках указанного вопроса. Так же есть возможность удалить выборку в
    вопросе. """
    serializer_class = ChoiceSerializer
    permission_classes = (permissions.IsAuthenticated,)

    @staticmethod
    def get_object(pk, choice_pk):
        try:
            return Choice.objects.filter(question_id=pk).get(pk=choice_pk)
        except Choice.DoesNotExist:
            raise Http404

    def get(self, request, pk, choice_pk, *args, **kwargs):
        choice = self.get_object(pk=pk, choice_pk=choice_pk)
        serializer = ChoiceSerializer(choice)
        return Response(serializer.data)

    def delete(self, request, pk, choice_pk, *args, **kwargs):
        choice = self.get_object(pk=pk, choice_pk=choice_pk)
        choice.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


