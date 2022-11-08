from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    questionnaire = models.ForeignKey('Questionnaire', on_delete=models.CASCADE, related_name='questions')
    # is_terminal = models.BooleanField(default=False)

    def __str__(self):
        return self.question_text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    answer_text = models.CharField(max_length=200)
    next_question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='next_question', blank=True,
                                      null=True)

    def __str__(self):
        return self.answer_text


class Questionnaire(models.Model):
    name = models.CharField(max_length=200)
    # questions = models.ForeignKey(Question, blank=True, symmetrical=False, related_name='questionnaire')

    def __str__(self):
        return self.name
