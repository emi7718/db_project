#from django.shortcuts import render  <<< this was here when I opened views.py for the 1st time
# Create your views here.

from django.http import HttpResponse, Http404
from .models import Question
from django.shortcuts import render


def index(request):
    latest_question_list = Question.objects.order_by('pub_date')[:5]
    context = {'latest_question_list':latest_question_list}   
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404('Question does not exist')
    return render(request, 'polls/detail.html', {'question':question})

def results(request, question_id):
    return HttpResponse('You\'re looking at the results of question %s' % question_id)

def vote(request, question_id):
    return HttpResponse('you\'re voting on question %s' % question_id)

