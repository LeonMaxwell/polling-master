from rest_framework import serializers
from questions.serializers import QuestionSerializer, PassedQuestionSerializer
from .models import User, Poll
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('pk', 'username', 'password')

class PollSerializer(serializers.ModelSerializer):
    quiz = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Poll
        fields = ('pk', 'name', 'description', 'created_at', 'finish_at', 'quiz')

    def update(self, instance, validated_data):
        if validated_data['created_at'] != instance.created_at:
            raise serializers.ValidationError({'created_at': 'Изменить дату начала опроса запрещено'})
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class PassedPollSerializer(serializers.ModelSerializer):
    quiz = PassedQuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Poll
        fields = ('pk', 'name', 'description', 'quiz')
