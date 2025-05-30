from rest_framework import generics
from .models import QuizQuestion
from .serializers import QuizQuestionSerializer

class QuizQuestionListView(generics.ListAPIView):
    queryset = QuizQuestion.objects.all()
    serializer_class = QuizQuestionSerializer
