from django.urls import path, include
from .views import *

app_name = 'questions' # Portfolio
urlpatterns = [
    path('question/comments/', include('django_comments.urls')),
]
