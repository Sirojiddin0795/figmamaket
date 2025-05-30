from django.db import models
from omonims.models import Omonim

class QuizQuestion(models.Model):
    omonim = models.ForeignKey(Omonim, on_delete=models.CASCADE, related_name='questions')
    question_text = models.TextField()

    def __str__(self):
        return f"Question about '{self.omonim.word}'"

class AnswerChoice(models.Model):
    question = models.ForeignKey(QuizQuestion, on_delete=models.CASCADE, related_name='choices')
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.text} ({'Correct' if self.is_correct else 'Wrong'})"
