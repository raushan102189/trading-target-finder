from multiprocessing.spawn import import_main_path
from re import template
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
def index(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    # context = {
    # 'latest_question_list': latest_question_list,
    # }
    return HttpResponse(template.render())


# def new(request):
#     return HttpResponse("Hello, world. You're at the raja new.")

# def home(render):
#     return render(render, 'polls/index.html')
def details(request):
    template = loader.get_template('polls/details.html')
    return HttpResponse(template.render())