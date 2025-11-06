import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def total_votes(self):
        votes = 0
        choices = self.choice_set.all()
        # Faça um laço para somar todos os votos.
        # models.IntegerField(default=0) garante que votes sempre terá um valor inteiro
        votes = sum(choice.votes for choice in choices)
        return votes

    def has_votes(self):
        # Utilize uma condição para retornar se essa Questão tem ou não votos.
        # devolve True mesmo quando a soma dos votos existem resulta em 0
        if self.choice_set.exclude(votes=0).exists() :
            return True
        return False


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
