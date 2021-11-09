from rest_framework import serializers

from questions.models import Question, Choice
from vote.serializers import SelectAnswerSerializer


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ('name', )


class QuestionSerializer(serializers.ModelSerializer):
    election = ChoiceSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ('pk', 'poll', 'text', 'type', 'election',)


class PassedQuestionSerializer(serializers.ModelSerializer):
    election = ChoiceSerializer(many=True, read_only=True)
    answer = SelectAnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ('pk', 'poll', 'text', 'type', 'election', 'answer', )