'''
A MARONE 09/22/2017
All rights reserved.
'''

from __future__ import unicode_literals

from django.db import models

#when changing question models we need to run command python manage.py makemigrations polls
# and then python manage.py migrate

class Question(models.Model):
	question_text = models.CharField(max_length=200) #field_example where is the pin? 
	pub_date = models.DateTimeField('date published')
	def __str__(self):
		return self.question_text
#here variables names are associated with COLUMN OF TABLE. CHOOSE NAMES WISELY
class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	#above is how relationships are defined with the foreign key, each choice is related with questions 
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
	def __str__(self):
		return self.choice_text

# Create your models here.
