# Load Questions from data.json
import os

from questionnaire.models import Question, Answer, Questionnaire
import json


def create_questionnaire(questionnaire):
    questionnaire = Questionnaire.objects.create(name=questionnaire['name'])
    question = questionnaire['questions']
    if not question['answers']:
        question_obj = create_question(question['question_text'], questionnaire, is_terminal=True)
        return None

    question_obj = create_question(question['question_text'], questionnaire)
    for answer in question['answers']:
        if answer['next_question']:
            next_question = create_question(answer['next_question'], questionnaire)
            create_answer(answer['answer_text'], question_obj, next_question)
    return questionnaire


def create_question(question_text, questionnaire):
    question_obj = Question.objects.create(question_text=question_text, questionnaire=questionnaire)
    return question_obj


def create_answer(answer_text, question, next_question=None):
    if next_question:
        answer_obj = Answer.objects.create(answer_text=answer_text, question=question, next_question=next_question)
    else:
        answer_obj = Answer.objects.create(answer_text=answer_text, question=question)
    return answer_obj


def load_data():
    json_file = open(os.path.join(os.path.dirname(__file__), 'data.json'))
    data = json.load(json_file)
    print(f'loaded data: {data}')
    questionnaire = Questionnaire.objects.create(name=data['questionnaire']['name'])
    create_recursively(data['questionnaire']['questions'], questionnaire)


def create_recursively(question, questionnaire):
    # if question:
    obj = Question.objects.create(question_text=question['question_text'], questionnaire=questionnaire)
    print(f'Question created: {obj}')

    for answer in question['answers']:
        next_question = create_recursively(answer['next_question'], questionnaire)
        answer = Answer.objects.create(question=obj, answer_text=answer['answer_text'], next_question=next_question)
        print(f'Answer created: {answer}, Next Question: {next_question}')
    return obj


load_data()
