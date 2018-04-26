from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader, RequestContext

from .models import Question


def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[:5]

    context = {
        'latest_questions':latest_questions
    }

    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    return HttpResponse("Detail view %s" % question_id)

def results(request, question_id):
    return HttpResponse("Result view %s" % question_id)

def votes(request, question_id):
    return HttpResponse("Votes %s" % question_id)

def home(request):
    return HttpResponse("Home")