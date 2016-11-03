from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render_to_response

import json

# Create your views here.
from django.utils import timezone
from questions.models import Question,Choice,Item,Location
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response, render, redirect
from django.template import Context, loader



def cors_json(resp):
	r = JsonResponse(resp)
	r['Access-Control-Allow-Origin'] = '*'
	r['Access-Control-Allow-Methods'] = "GET"
	r['Access-Control-Allow-Headers'] = 'X-Requested-With,content-type'
	return r

@csrf_exempt
def index(request):
	return redirect(resdevices)
    #return render_to_response('app/index.html')
   # return HttpResponse("QUESTIONS PAGE")
#security error fix later

#SETHS


def devices(request):
	dev = Item.objects.all()
	items = {"devices":dev}
	return render(request,'questions/devices.html',items)

def locations(request):
    loc = Location.objects.all()
    itm = []
    for i in loc:
        itm.append(len(Item.objects.filter(loc_ass=i)))

    items = {"Location":list(zip(loc,itm))}

    return render(request,'questions/location.html',items)

def locationsadd(request):

	return render(request, 'questions/location_form.html', {})

def deviceView(request,dev_pk):

	return HttpResponse("<h2>  Device {} </h2>".format(dev_pk))

def locationView(request,loc_pk):
	#<!--{% #url 'questions:deviceView' loc.0.id %}-->
	name = Location.objects.filter(id=loc_pk)
	ims = Item.objects.filter(loc_ass=name)
	inspctor = ""
	if ims:
		inspctor = ims[0].user_assigned
	things = {
	'name': name,
	'inspctor':inspctor,
	'items':ims
	}
	return render(request, 'questions/location-view.html', things)

@csrf_exempt
def addlocation(request):
	if request.method == 'POST':
		received_json_data=json.loads(request.body)
		loc_barcode=received_json_data["loc_barcode_num"]
		loc_barcode_name=received_json_data["loc_barcode_name"]
		items=received_json_data["items"]
		questions_for_loc_only=received_json_data["loc_questions"]

		location=Location.objects.create(loc_barcode_num=loc_barcode, loc_name=loc_barcode_name)

		for item in items:
			sql_item= location.item_set.create(item_barcode_num=item["barcode_num"], item_type=item["item_type"], admin=item["admin"], user_assigned=item["user_assigned"])
			for question in item["questions"]:
				q= sql_item.question_set.create(question_text=question, pub_date=timezone.now())
			location.item_set.add(sql_item)
		for locquest in questions_for_loc_only:
			location.question_set.create(question_text=locquest, pub_date=timezone.now())
		return cors_json({'data': location.get_json_object()}) #THIS SHOULD JUST SAY GOOODBYE OR GOOD DATA

def add(request):
	if request.method == 'POST':
			q= Question(question_text=request.POST["question_text"], pub_date=timezone.now())
			q.save()
			return HttpResponse("Good work homie")


#KYLES
@csrf_exempt
def questionsbyuser(request):
	if request.method == 'POST':
		user=request.POST["user"]
		filtered_items=Location.objects.filter(item__user_assigned=user)
		#print filtered_items, "FILTERED"
		return cors_json({'data': map (Location.get_json_object, filtered_items)})

@csrf_exempt
def addanswers(request):
	if request.method == 'POST':
		received_json_data=json.loads(request.body)["data"]
		for loc_assessed in received_json_data:
			loc_barcode=loc_assessed["barcode_num"]
			location_entry=Location.objects.get(loc_barcode_num=loc_barcode)
			questions_for_loc_only=loc_assessed["loc_questions"]
			items=loc_assessed["items"]
			for item in items:
				time_scanned=item["time_scanned"]
				item_barcode=item["barcode_num"]
				person_scanned=item["person_scanned"]
				item_questions=item["questions"]
				item_entry=location_entry.item_set.get(item_barcode_num=item_barcode)

				location_entry.item_set.filter(item_barcode_num = item_barcode).update(person_scanned=person_scanned)
				location_entry.item_set.filter(item_barcode_num = item_barcode).update(time_scanned=time_scanned)
				for question in item_questions:
					question_real=item_entry.question_set.get(question_text=question["question_text"])
					question_real.choice_set.create(choice_text=question["question_answer"])
			for question in questions_for_loc_only:
				question_real=location_entry.question_set.get(question_text=question["question_text"])
				question_real.choice_set.create(choice_text=question["question_answer"])

		return HttpResponse("Good work homie")
