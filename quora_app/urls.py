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
    path('vote/' ,views.upvote ,name='upvote'),
    #path('<int:question_id>/vote/', views.downvote, name='downvote'),
]
