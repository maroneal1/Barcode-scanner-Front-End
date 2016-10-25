'''
A MARONE 09/22/2017
All rights reserved.
'''

from __future__ import unicode_literals

from django.db import models

#when changing question models we need to run command python manage.py makemigrations polls
# and then python manage.py migrate

'''
TOP DOWN APPROACH 
'''

#Question is here do we want admins assigned to locations, 
#like should locations be another class? 
#dont think we need. 
class Location(models.Model):
	loc_barcode_num = models.IntegerField(default=0)
	loc_name = models.CharField(max_length=200)#floor1basement
	def __str__(self):
		return self.loc_name + str(self.loc_barcode_num) + str(self.item_set.all()) + str(self.question_set.all()) 
	#questions_loc=models.ForeignKey( Question, on_delete=models.CASCADE)
	#items=models.ForeignKey( Item, on_delete=models.CASCADE)
	#questions,
	#items
	#admins
	#human readbale field 


class Item(models.Model):
	item_name = models.CharField(max_length=200)#example fire equitunisher
	item_barcode_num=models.IntegerField(default=0)
	#loc_barcode_num=models.IntegerField(default=0)
	item_type = models.CharField(max_length=200)
	user_assigned = models.CharField(max_length=200) 
	admin = models.CharField(max_length=200) #should actually be payroll id 
	#questions=models.ForeignKey( Question, on_delete=models.CASCADE)
	loc_ass=models.ForeignKey( Location, on_delete=models.CASCADE)
	def __str__(self):
		return str(self.item_barcode_num)


class Question(models.Model):
	question_text = models.CharField(max_length=200) #field_example where is the pin? 
	pub_date = models.DateTimeField('date published') #this is obtained from ADMIN
	#answers= models.ForeignKey( Choice, on_delete=models.CASCADE) #posted by users 
	item_assoc=models.ForeignKey( Item, on_delete=models.CASCADE, null=True)
	questions_loc=models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
	def __str__(self):
		return self.question_text


class Choice(models.Model):
	##question = models.ForeignKey(Question, on_delete=models.CASCADE)
	#above is how relationships are defined with the foreign key, each choice is related with questions 
	choice_text = models.CharField(max_length=200)
	scan_date_time = models.DateTimeField('datetime answered') #this is obtained from ADMIN
	person_scanned = models.CharField(max_length=200)
	question_associated_with= models.ForeignKey( Question, on_delete=models.CASCADE) #posted by users 
	##votes = models.IntegerField(default=0)
	def __str__(self):
		return self.choice_text

#here variables names are associated with COLUMN OF TABLE. CHOOSE NAMES WISELY



# Create your models here.
