from django.urls import path
from .views import QuizQuestionListView

urlpatterns = [
    path('questions/', QuizQuestionListView.as_view()),
]
