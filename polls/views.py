from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404 
from django.template import loader
from .models import Question

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list':latest_question_list}
    return render(request,'polls/index.html',context)

def detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    return render(request,'polls/detail.html',{'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("<h1>You're voting on question %s.</h1>" % question_id)


