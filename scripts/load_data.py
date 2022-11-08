#Load Questionnare from Json
import json
from questionnaire.models import Question, Answer, Questionnaire

with open('.//data.json') as f:
    data = json.load(f)

    for questionnaire in data:
        questionnaire_obj = Questionnaire.objects.create(name=questionnaire['name'])
        for question in questionnaire['questions']:
            question_obj = Question.objects.create(question_text=question['question_text'], questionnaire=questionnaire_obj)
            for answer in question['answers']:
                Answer.objects.create(question=question_obj, answer_text=answer['answer_text'])
