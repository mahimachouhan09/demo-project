# 1. Import python packages
# 2. Django imports
# 3. app imports
# 4. Current app imports
# 5. Utility imports

from datetime import date
from django.shortcuts import render,  redirect
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models import Q
from .forms import CustomSignupForm,TopiclistForm ,QuestionForm, AnswerForm ,ActivityForm
from .models import Activity, Answer, Topic, Profile,Question

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
    if "search" in request.GET:
        search_query = request.GET['search']
        questions = Question.objects.filter(Q(question__icontains=search_query) | Q(topic__name__icontains= search_query))
    return render(request, 'question_list.html', {'questions': questions })

def answer_list(request, question_id ):
    question = Question.objects.get(pk = question_id)
    return render(request, 'answer_list.html', {'question': question})

def add_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
           form.save()
        return redirect(reverse('quora_app:question_list'))
    form = QuestionForm(initial= {'user': request.user.id })
    return render(request, 'add_question.html', {'form': form})

def add_answer(request,question_id):
    if request.method == 'POST':
        form = AnswerForm(request.POST )
        if form.is_valid():
            form.save()
        return redirect(reverse('quora_app:question_list'))
    form = AnswerForm(initial= {'user': request.user.id ,'question':question_id })
    return render(request, 'add_answer.html', {'form': form})

def upvote(request,object_id):
    if request.GET.get('cb') == 'Question':
        question = Question.objects.get(pk=object_id)
        Activity.objects.create(content_object=question, activity_type=Activity.UP_VOTE, user=request.user.profile)
        return redirect(reverse('quora_app:question_list'))
    elif request.GET.get('cb') == 'Answer':
        answer = Answer.objects.get(pk=object_id)
        Activity.objects.create(content_object=answer, activity_type=Activity.UP_VOTE, user=request.user.profile)
        return redirect(reverse('quora_app:answer_list' , args=[answer.question.id]))

def downvote(request,object_id):
    if request.GET.get('cb') == 'Question':
        question = Question.objects.get(pk=object_id)
        Activity.objects.create(content_object=question, activity_type=Activity.DOWN_VOTE, user=request.user.profile)
        return redirect(reverse('quora_app:question_list'))
    elif request.GET.get('cb') == 'Answer':
        answer = Answer.objects.get(pk=object_id)
        Activity.objects.create(content_object=answer, activity_type=Activity.DOWN_VOTE, user=request.user.profile)
        return redirect(reverse('quora_app:answer_list' , args=[answer.question.id]))

