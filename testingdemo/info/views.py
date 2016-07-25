from django.shortcuts import render,redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
from django.http import HttpResponse
from models import person
from models import quiz
def hello(request):
    retrieve = person.objects.all()
    paginator = Paginator(retrieve, 1)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        images = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        images = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        images = paginator.page(paginator.num_pages)

    return render(request, 'info/index.html', {'persondata': images})


def quiz(request):
    retrieve=quiz.objects.all()
    paginator = Paginator(retrieve, 1)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        questions = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        questions = paginator.page(paginator.num_pages)

    return render(request, 'info/quiz.html', {'questions': questions})







