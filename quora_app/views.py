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
    #import pdb;pdb.set_trace()
    questions = Question.objects.all()
    return render(request, 'question_list.html', {'questions': questions })

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

def upvote(request):
    if request.method == 'POST':
        form = ActivityForm(request.POST)
        # my_model = ContentType.objects.get(app_label='quora_app', model='Activity')
        # object = my_model.id
        if content_object == Question:
        #activity = Activity.objects.create(content_object=question, activity_type=Activity.UP_VOTE, user=user)
            if form.is_valid():
                form.user = request.user
                form.question = request.content_type[request.POST]
                form.activity_type = request.POST
                for question1 in question:
                    question1.vote += 1
                    form.save()
        return redirect(reverse('/'))

        # else:
        #     content = request.POST
        #     if form.is_valid():
        #         #form.vote.set(Activity.objects.all())`
        #         form.question = request.content_object['answer']
        #         form.activity_type = request.POST
        #         for answer in content:
        #             answer.vote += 1
        #             form.save()
        #     return redirect(reverse('quora_app:question_list'))

    form = ActivityForm(initial= {'user': request.user.id })
    return render(request, 'upvote.html', {'form': form})