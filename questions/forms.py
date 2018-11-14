from django.contrib import admin
from django.forms import ModelForm, Textarea
from .models import *

class QuestionForm(ModelForm):
	class Meta:
		fields = '__all__'
		model = Question

class DiscussionQuestionForm(ModelForm):
	class Meta:
		fields = ('comment',)
		model = DiscussionQuestion

	# def save(self):
	# 	DiscussionQuestion.objects.rebuild()
	# 	return super(DiscussionQuestionForm, self).save(*args, **kwargs)    

