from django.shortcuts import render,  redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Activity, Answer, Follow, Topic, Profile,Question
from django.urls import reverse
from .forms import SignupForm, LoginForm,TopiclistForm ,QuestionForm, AnswerForm ,ActivityForm
from django.contrib.auth import login, authenticate
from datetime import date
from django.contrib.contenttypes.models import ContentType
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

def answer_list(request,question_id):
    #import pdb;pdb.set_trace()
    answer = Answer.objects.all()
    return render(request, 'answer_list.html', {'answer': answer })

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
    return redirect(reverse('quora_app:question_list'))

def downvote(request,object_id):
    import pdb;pdb.set_trace()
    if request.GET.get('cb') == 'Question':
        question = Question.objects.get(pk=object_id)
        Activity.objects.create(content_object=question, activity_type=Activity.DOWN_VOTE, user=request.user.profile)
        return redirect(reverse('quora_app:question_list'))
    elif request.GET.get('cb') == 'Answer':
        answer = Answer.objects.get(pk=object_id)
        Activity.objects.create(content_object=answer, activity_type=Activity.DOWN_VOTE, user=request.user.profile)
    return redirect(reverse('quora_app:question_list'))

def totalvote(request,object_id):
    pass