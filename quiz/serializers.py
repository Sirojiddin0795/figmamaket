from rest_framework import serializers
from .models import QuizQuestion, AnswerChoice

class AnswerChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerChoice
        fields = ['id', 'text', 'is_correct']

class QuizQuestionSerializer(serializers.ModelSerializer):
    choices = AnswerChoiceSerializer(many=True, read_only=True)

    class Meta:
        model = QuizQuestion
        fields = ['id', 'omonim', 'question_text', 'choices']
