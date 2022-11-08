from django.urls import path, include

from .views import QuestionnaireViewset, QuestionViewset, AnswerViewset, LoggerView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', QuestionnaireViewset, basename='questionnaire')
router.register(r'question', QuestionViewset, basename='question')
router.register(r'answer', AnswerViewset, basename='answer')

urlpatterns = [path('logger/', LoggerView.as_view()),
               path('', include(router.urls))]
