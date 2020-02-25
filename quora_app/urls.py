from django.urls import path
from django.views import generic
from . import views

app_name = 'quora_app'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('topic/', views.select_topic, name='topic'),
    path('add_question/' ,views.add_question, name='add_question'),
    path('add_answer/' ,views.add_answer , name= 'add_answer'),
    path('question_list/' ,views.question_list , name= 'question_list'),
    #path('index/<int:question_id>' ,views.add_answer , name= 'add_answer'),
    path('vote/<int:object_id>/', views.upvote, name='upvote'),
    path('vote/<int:object_id>/', views.downvote, name='downvote'),
    path('vote/<int:object_id>/', views.totalvote, name='totalvote'),
    path('answer_list/<int:question_id>/', views.answer_list, name='answer_list'),
]
