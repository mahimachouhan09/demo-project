# 1. Import python packages
# 2. Django imports
# 3. app imports
# 4. Current app imports
# 5. Utility imports

from datetime import date
from django.shortcuts import render,  redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.contenttypes.models import ContentType

from .forms import TopiclistForm ,QuestionForm, AnswerForm ,ActivityForm
from .models import Activity, Answer, Topic, Profile,Question

# Create your views here.

def index(request):
    return render(request, 'index.html')

def select_topic(request):
    if request.method == 'POST':
        form = TopiclistForm(request.POST)
        if form.is_valid():
            form.save(request)
        return redirect(reverse('quora_app:index'))
    form = TopiclistForm()
    return render(request , 'topic.html' ,{'form':form} )

def question_list(request):
    questions = Question.objects.all()
    return render(request, 'question_list.html', {'questions': questions })

def answer_list(request, question_id):
    question = Question.objects.get(pk = question_id)
    return render(request, 'answer_list.html', {'question': question})

# def add_question(request):
#     if request.method == 'POST':
#         form = QuestionForm(request.POST)
#         if form.is_valid():
#            form.save(commit=False)
#            form.user = request.user
#            form.save()
#         return redirect(reverse('quora_app:question_list'))
#     form = QuestionForm()
#     return render(request, 'add_question.html', {'form': form})

def add_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
           form.save()
        return redirect(reverse('quora_app:question_list'))
    form = QuestionForm(initial= {'user': request.user.id })
    return render(request, 'add_question.html', {'form': form})

def add_answer(request):
    if request.method == 'POST':
        form = AnswerForm(request.POST )
        if form.is_valid():
            form.save()
        return redirect(reverse('quora_app:question_list'))
    form = AnswerForm(initial= {'user': request.user.id })
    return render(request, 'add_answer.html', {'form': form})

def upvote(request,object_id):
    if request.GET.get('cb') == 'Question':
        question = Question.objects.get(pk=object_id)
        Activity.objects.create(content_object=question, activity_type=Activity.UP_VOTE, user=request.user.profile)
        return redirect(reverse('quora_app:question_list'))
    elif request.GET.get('cb') == 'Answer':
        answer = Answer.objects.get(pk=object_id)
        Activity.objects.create(content_object=answer, activity_type=Activity.UP_VOTE, user=request.user.profile)
    return redirect(reverse('quora_app:answer_list' , args=[object_id]))

def downvote(request,object_id):
    if request.GET.get('cb') == 'Question':
        question = Question.objects.get(pk=object_id)
        Activity.objects.create(content_object=question, activity_type=Activity.DOWN_VOTE, user=request.user.profile)
        return redirect(reverse('quora_app:question_list'))
    elif request.GET.get('cb') == 'Answer':
        answer = Answer.objects.get(pk=object_id)
        Activity.objects.create(content_object=answer, activity_type=Activity.DOWN_VOTE, user=request.user.profile)
    return redirect(reverse('quora_app:answer_list' , args=[object_id]))

def totalvote(request,object_id):
    #totalvote = object_id.upvote - object_id.downvote
    pass