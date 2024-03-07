from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from vege.models import *
# Create your views here.
def home(request):
    queryset = Receipe.objects.all()
    context = {'queryset': queryset}
    return render(request, 'index.html',context)

def detail(request, student_id):
    return HttpResponse("You're looking at question %s." % student_id)

def results(request):
    return HttpResponse("You're looking at question.")


# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     template = loader.get_template("polls/index.html")
#     context = {
#         "latest_question_list": latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))

# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     context = {"latest_question_list": latest_question_list}
#     return render(request, "polls/index.html", context)

# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, "polls/detail.html", {"question": question})