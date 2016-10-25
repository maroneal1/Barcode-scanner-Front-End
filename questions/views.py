from django.http import HttpResponse
import json

# Create your views here.
from django.utils import timezone
from questions.models import Question,Choice,Item,Location
from django.views.decorators.csrf import csrf_exempt
#https://docs.djangoproject.com/en/1.10/intro/tutorial03/


def index(request):
    return HttpResponse("QUESTIONS PAGE")
#security error fix later

#SETHS

@csrf_exempt
def addlocation(request):
	if request.method == 'POST':

		received_json_data=json.loads(request.body)
		print (received_json_data)
		
		loc_barcode=received_json_data["loc_barcode_num"]
		items=received_json_data["items"]
		questions_for_loc_only=received_json_data["loc_questions"]
		
		location=Location.objects.create(loc_barcode_num=loc_barcode)
		
		
		for item in items:
			sql_item= location.item_set.create(item_barcode_num=item["barcode_num"], item_type=item["item_type"])
			for question in item["questions"]:
				q= sql_item.question_set.create(question_text=question, pub_date=timezone.now())
			location.item_set.add(sql_item)
		for locquest in questions_for_loc_only:
			location.question_set.create(question_text=locquest, pub_date=timezone.now())

		print (Location.objects.all())
		return HttpResponse(request.POST)
	
def add(request):
	if request.method == 'GET':
#		return HttpResponse(Question.objects.all()) # need to filter by user 
		taco=3
		#do nothing. 
	elif request.method == 'POST':
		q= Question(question_text=request.POST["question_text"], pub_date=timezone.now())
		q.save()
		return HttpResponse("Good work homie")

#KYLES
@csrf_exempt
def questionsbyuser(request):
	if request.method == 'GET':
		print (Location.objects.all())
		return HttpResponse(Location.objects.all()) # need to filter by user 
	
	elif request.method == 'POST':
		user=request.POST["user"]
		#field has to be posted as user
		return HttpResponse(Question.objects.all()) # need to filter by user 
