import django
import os

#https://docs.djangoproject.com/en/1.10/intro/tutorial02/

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
django.setup()
from questions.models import Question, Choice
print Question.objects.all()
print Question.objects.filter(id=1)
print Question.objects.filter(question_text__startswith='W')
q = Question.objects.get(pk=1)
print q, " IS QUESTION"
print q.choice_set.all(), "IS POSSIBLE CHOices"
