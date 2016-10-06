from django.http import HttpResponse

# Create your views here.
from django.utils import timezone
from questions.models import Question,Choice
from django.views.decorators.csrf import csrf_exempt
#https://docs.djangoproject.com/en/1.10/intro/tutorial03/
def index(request):
    return HttpResponse("QUESTIONS PAGE")
#security error fix later
@csrf_exempt
def add(request):
	if request.method == 'GET':
		taco=3
		#do nothing. 
	elif request.method == 'POST':
		q= Question(question_text=request.POST["question_text"], pub_date=timezone.now())
		q.save()
		return HttpResponse("Good work homie")
