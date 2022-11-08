from rest_framework import serializers

from .models import Questionnaire, Question, Answer


class QuestionnaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questionnaire
        fields = ('id', 'name')


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'answer_text')


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer( many=True, read_only=True)

    class Meta:
        model = Question
        fields = ('id', 'question_text', 'answers')


