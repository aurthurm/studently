from django.contrib import admin
from .models import Question, DiscussionQuestion
from .forms import QuestionForm, DiscussionQuestionForm


class QuestionAdmin(admin.ModelAdmin):
    form = QuestionForm

admin.site.register(Question, QuestionAdmin)
admin.site.register(DiscussionQuestion)