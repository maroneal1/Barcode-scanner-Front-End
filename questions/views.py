from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login,logout
from django.views import View

import json

# Create your views here.
from django.utils import timezone
from questions.models import Question,Choice,Item,Location,Device,LocDev
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response, render, redirect
from django.template import Context, loader
from questions.CustomContainers import User,UserFactory
from django.utils.decorators import method_decorator


def cors_json(resp):
	print(resp)
	r = JsonResponse(resp)
	r['Access-Control-Allow-Origin'] = '*'
	r['Access-Control-Allow-Methods'] = "GET"
	r['Access-Control-Allow-Headers'] = 'X-Requested-With,content-type'
	return r

@csrf_exempt
def index(request):
	return redirect(resdevices)

def logout_view(request):
    logout(request)
    # Redirect to a success page.



#@login_required
def devices(request):
	dev = list(Device.objects.all())
	dev.sort()
	items = {"devices":dev}
	return render(request,'questions/devices.html',items)

def locations(request):
    loc = Location.objects.all()
    items = {"Location":loc,}
    return render(request,'questions/location.html',items)

def users(request):
	return render(request,'questions/users.html',{'usrs':UserFactory()})

def locationsadd(request):
	dev = Device.objects.all()
	items = {"devices":dev}
	return render(request, 'questions/location_form.html', items)

def deviceadd(request):
	return render(request, 'questions/device_add.html', {})

def recent_scaned(ques,n):
	out =[ int(q.time_scanned) for q in ques]
	out.sort()
	return out[-n:]

class deviceView(View):
	@method_decorator(csrf_exempt)
	def dispatch(self, request, dev_pk):
		return super(deviceView, self).dispatch(request, dev_pk)
	def get(self, request,dev_pk):
		dev = Device.objects.get(id=dev_pk)
		itms = Item.objects.filter(item_type=dev)
		things = {'device': dev,'items':itms, 'dev_pk':dev_pk}
		return render(request, 'questions/device-view.html', things)
	def post(self, request,dev_pk):
		received_json_data=json.loads(request.body)
		Item.objects.create(item_type=Device.objects.get(id=dev_pk),
							item_barcode_num=received_json_data["barcode"])
		return HttpResponse("Correct")

def locationView(request,loc_pk):
	#<!--{% #url 'questions:deviceView' loc.0.id %}-->
	location = Location.objects.get(id=loc_pk)
	maping = LocDev.objects.filter(location=location)
	#Device.objects.get(pk=
	device = [Device.objects.get(pk=i.device.pk) for i in maping ]
	lcoansers = ""#recent_scaned(Choice.objects.filter(location=location),1)
	devansers = []
	#for device in devices:
		#devansers.append(Choice.object.filter(device))
	things = {
	'location': location,
	}
	return render(request, 'questions/location-view.html', things)

#SETHS

#URL TO POST DEVICE TO, creates questions there
#GETDEVICES URL-> send key from DB.


@csrf_exempt
def adddevice(request):
	if request.method == 'POST':
		received_json_data=json.loads(request.body)
		device_name=received_json_data["device_name"]
		manu=received_json_data["manu"]
		type_equip=received_json_data["type"]
		model_number=received_json_data["model_number"]
		questions_for_the_device=received_json_data["questions"]
		barcodes=received_json_data["barcodes"]

		new_device=Device.objects.create(device_name=device_name, manufacturer=manu, type_equip=type_equip, model_number=model_number)
		for barcode in barcodes:
			new_device.item_set.create(item_barcode_num=barcode)
		for question in questions_for_the_device:
			new_device.question_set.create(question_text=question)
		new_device.save()
		return HttpResponse("Good work homie" + str(new_device.id))




#WHEN SETH WANTS THIS OD IT
@csrf_exempt
def addlocation(request):
	if request.method == 'POST':
		received_json_data=json.loads(request.body)
		loc_barcode=received_json_data["loc_barcode_num"]
		loc_name=received_json_data["loc_name"]
		user_assigned=received_json_data["user_assigned"]
		questions_for_loc_only=received_json_data["loc_questions"]
		devices_to_add=received_json_data["devices_to_add"]

		location=Location.objects.create(loc_barcode_num=loc_barcode, loc_name=loc_name, user_assigned=user_assigned)

		for locquest in questions_for_loc_only:
			location.question_set.create(question_text=locquest)
		for device_id in devices_to_add:
			print (device_id , "is device_id")
			print(Device.objects.all(), "sfgsdf ", device_id)
			print(int(device_id))
			found_device=Device.objects.get(id=int(device_id))
			print (found_device)
			LocDev.objects.create(location=location, device=found_device) #Check me

		return HttpResponse("Correct")


#KYLES
@csrf_exempt
def questionsbyuser(request):
	if request.method == 'POST':
		user=request.POST["user"]
		filtered_items=Location.objects.all()
		return cors_json({'data': map (Location.get_json_object, filtered_items)})

@csrf_exempt
def addanswers(request):
	if request.method == 'POST':
		received_json_data=json.loads(request.body)["data"]
		answers=received_json_data["answers"]
		for answer in answers:
			time_answered= int(answer["time_answered"])
			loc_id=answer["loc_id"]
			user=answer["user"]
			answer_text=answer["answer_text"]

			if "question_id" in answer:
				question_id=answer["question_id"]
				question_entry=Question.objects.get(id=question_id)
			else:
				taco= "I am a note"
			question_entry.choice_set.create(choice_text=answer_text, person_scanned=user, time_scanned=time_answered)

		return HttpResponse("Good work homie")
