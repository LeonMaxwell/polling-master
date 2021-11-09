from rest_framework import serializers

from .models import Answer


class AnswerSerializer(serializers.ModelSerializer):
    anon = serializers.BooleanField(write_only=True)

    class Meta:
        model = Answer
        fields = ('pk', 'question', 'text', 'anon',)

    def to_representation(self, instance):
        ret = super(AnswerSerializer, self).to_representation(instance)
        if self.validated_data['anon']:
            answers = Answer.objects.all()
            user_id = 1
            for answer in answers:
                if answer.pk == user_id:
                    user_id += 1
                elif answer.pk > user_id:
                    user_id = answer.pk
            ret['user_id'] = f"anonymous_{user_id}"
        else:
            ret['user_id'] = self.root.instance.user_id
        return ret

    def create(self, validated_data):
        return Answer.objects.create(
            user=self.context['request'].user,
            question=validated_data['question'],
            text=validated_data['text'], )


class SelectAnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ('pk', 'text', )