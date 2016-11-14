from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login,logout

import json

# Create your views here.
from django.utils import timezone
from questions.models import Question,Choice,Item,Location,Device,LocDev
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response, render, redirect
from django.template import Context, loader



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
	dev = Device.objects.all()
	items = {"devices":dev}
	return render(request,'questions/devices.html',items)

def locations(request):
    loc = Location.objects.all()
    items = {"Location":loc,}
    return render(request,'questions/location.html',items)

def users(request):
	return render(request,'questions/users.html')

def locationsadd(request):
	return render(request, 'questions/location_form.html', {})

def deviceadd(request):
	return render(request, 'questions/device_add.html', {})

def recent_scaned(ques,n):
	out =[ int(q.time_scanned) for q in ques]
	out.sort()
	return out[-n:]

def deviceView(request,dev_pk):
	things = {'device': Device.objects.get(id=dev_pk)}
	return render(request, 'questions/device-view.html', things)

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

		new_device=Device.objects.create(device_name=device_name, manufacturer=manu, type_equip=type_equip, model_number=model_number)

		new_device.save()
		for question in questions_for_the_device:
			new_device.question_set.create(question_text=question)
		return HttpResponse("Good work homie" + str(new_device.id))




#WHEN SETH WANTS THIS OD IT
@csrf_exempt
def addlocation(request):
	if request.method == 'POST':
		received_json_data=json.loads(request.body)
		loc_barcode=received_json_data["loc_barcode_num"]
		loc_name=received_json_data["loc_name"]
		questions_for_loc_only=received_json_data["loc_questions"]
		devices_to_add=received_json_data["devices_to_add"]

		location=Location.objects.create(loc_barcode_num=loc_barcode, loc_name=loc_name)
		locdev=LocDev.objects.create() #location for locdev obj = self

		for locquest in questions_for_loc_only:
			location.question_set.create(question_text=locquest)
		for device_id in devices_to_add:
			print (device_id , "is device_id")
			print(Device.objects.all(), "sfgsdf ", device_id)
			print(int(device_id))
			found_device=Device.objects.get(pk=int(device_id))
			#found_device=Device.objects.get(id=device_id)
			print (found_device , "is device_id")

#what we can do here is print the object with a device_object.id
			LocDev.objects.create(location=location, device=found_device) #Check me
			#found_device.location_set.create()
			#found_device.locdev_set.create(dummy_field=1)
			#locdev.device.create(device=device_id)
		#locdev.location_set.create(location)
	#	location.locdev_set.create(dummy_field=1)
		return HttpResponse("Correct")

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
		#filtered_items=Location.objects.filter(item__user_assigned=user)
		#filtered_items=Location.objects.all()
		filtered_items=LocDev.objects.all()
		return cors_json({'data': map (LocDev.get_json_object, filtered_items)})
		#return cors_json({'data': map (Location.get_json_object, filtered_items)})

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
