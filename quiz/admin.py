from django.contrib import admin
from .models import QuizQuestion, AnswerChoice

class AnswerChoiceInline(admin.TabularInline):
    model = AnswerChoice
    extra = 2

@admin.register(QuizQuestion)
class QuizQuestionAdmin(admin.ModelAdmin):
    list_display = ['question_text', 'omonim']
    inlines = [AnswerChoiceInline]

@admin.register(AnswerChoice)
class AnswerChoiceAdmin(admin.ModelAdmin):
    list_display = ['text', 'is_correct', 'question']
