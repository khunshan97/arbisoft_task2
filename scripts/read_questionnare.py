from questionnaire.models import Question, Answer, Questionnaire

choices = ['yes', 'pizza']



def check_flow(q):
    
    stack = [q]
    while stack:
        question = stack.pop()
        print('Question',question.question_text)
        answers = question.answers.all()

        
        for answer in answers:
            stack.append(answer.next_question)


questionnaire = Questionnaire.objects.get(id=4)
check_flow(questionnaire.questions.first())
