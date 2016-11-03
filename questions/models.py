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



#ADD JSON REPONSE WITH DJANGO



#Question is here do we want admins assigned to locations,
#like should locations be another class?
#dont think we need.

class Location(models.Model):
	loc_barcode_num = models.IntegerField(default=0)
	loc_name = models.CharField(max_length=200, default= " ")#floor1basement
	admin = models.CharField(max_length=200) #should actually be payroll id
	user_assigned = models.CharField(max_length=200)
	def get_json_object(self):
		def access_lower_object_json(key):
			return key.get_json_object()
		ret={}
		ret["barcode_num"]=self.loc_barcode_num
		ret["loc_barcode_name"]=self.loc_name
		ret["items"]=map(access_lower_object_json, self.item_set.all())
		ret["loc_questions"]=map(access_lower_object_json, self.question_set.all())
		return ret
	def __str__(self):
		return str(self.loc_barcode_num)

class LocDev(models.Model):
	location=models.ForeignKey( Location, on_delete=models.CASCADE)
	device=models.ForeignKey( Device, on_delete=models.CASCADE)

class Device(models.Model):
	device_name = models.CharField(max_length=200)
	manufacturer = models.CharField(max_length=200)
	model_number = models.CharField(max_length=200)
	admin = models.CharField(max_length=200) #should actually be payroll id

class Item(models.Model):
	item_name = device=models.ForeignKey( Device, on_delete=models.CASCADE)
	item_barcode_num = models.IntegerField(default=0)
	item_type=models.ForeignKey( Device, on_delete=models.CASCADE)
	user_assigned=models.CharField(max_length=200)
	admin=models.CharField(max_length=200) #should actually be payroll id

	def get_json_object(self):
		def access_lower_object_json(key):
			return key.get_json_object()
		ret ={}
		ret["barcode_num"]=self.item_barcode_num
		ret["item_type"]=self.item_type
		ret["user_assigned"]=self.user_assigned
		ret["time_scanned"]=self.time_scanned
		ret["admin"]=self.admin
		ret["questions"]=map(access_lower_object_json, self.question_set.all())
		return ret
	def __str__(self):
		return str(self.item_barcode_num)


class Question(models.Model):
	question_text = models.CharField(max_length=200) #field_example where is the pin?
	pub_date = models.DateTimeField('date published') #this is obtained from ADMIN
	item_assoc=models.ForeignKey( Item, on_delete=models.CASCADE, null=True)
	questions_loc=models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
	def get_json_object(self):
		ret ={}
		ret["question_text"]=self.question_text
		return ret
	def __str__(self):
		return self.question_text


class Choice(models.Model):
	#above is how relationships are defined with the foreign key, each choice is related with questions
	choice_text = models.CharField(max_length=200)
	time_scanned=models.CharField(max_length=200, default= " ")
	person_scanned=models.CharField(max_length=200, default= " ")
	question= models.ForeignKey( Question, on_delete=models.CASCADE) #posted by users
	location= models.ForeignKey( Location, on_delete=models.CASCADE) #posted by users
	def __str__(self):
		return self.choice_text

#here variables names are associated with COLUMN OF TABLE. CHOOSE NAMES WISELY



# Create your models here.
