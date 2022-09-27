#from django.shortcuts import render  <<< this was here when I opened views.py for the 1st time
# Create your views here.

from django.template import loader
from django.http import HttpResponse
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    return HttpResponse('You\'re looking at question %s.' % question_id)

def results(request, question_id):
    return HttpResponse('You\'re looking at the results of question %s' % question_id)

def vote(request, question_id):
    return HttpResponse('you\'re voting on question %s' % question_id)

