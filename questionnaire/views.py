from rest_framework import viewsets, views
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from .serializers import QuestionnaireSerializer, QuestionSerializer, AnswerSerializer
from .models import Questionnaire, Question, Answer


class QuestionnaireViewset(viewsets.ViewSet):
    def list(self, request):
        queryset = Questionnaire.objects.all()
        serializer = QuestionnaireSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Questionnaire.objects.all()
        questionnaire = get_object_or_404(queryset, pk=pk)
        serializer = QuestionnaireSerializer(questionnaire).data
        question_data = QuestionSerializer(questionnaire.questions.first()).data
        # serializer.data['questions'] = [question_data]
        serializer.update({"question": question_data})
        return Response(serializer)


class QuestionViewset(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        queryset = Question.objects.all()
        question = get_object_or_404(queryset, pk=pk)
        serializer = QuestionSerializer(question)
        return Response(serializer.data)


class AnswerViewset(viewsets.ViewSet):

    def retrieve(self, request, pk=None):
        answer = get_object_or_404(Answer, pk=pk)
        serializer = QuestionSerializer(answer.next_question)
        return Response(serializer.data)


class LoggerView(views.APIView):
    # print('ok')
    def post(self, request):
        print(request.data)
        questionnaire = Questionnaire.objects.get(pk=request.data['questionnaire']).questions.first()
        choices = request.data['choices']
        print(questionnaire, choices)

        return Response('ok')
