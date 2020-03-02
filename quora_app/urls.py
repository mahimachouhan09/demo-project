from django.urls import path
from . import views

app_name = 'quora_app'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('topic/', views.select_topic, name='topic'),
    path('add_question/' ,views.add_question, name='add_question'),
    path('<int:question_id>/add_answer/' ,views.add_answer , name= 'add_answer'),
    path('question_list/' ,views.question_list , name= 'question_list'),
    path('<int:object_id>/upvote/', views.upvote, name='upvote'),
    path('downvote/<int:object_id>/', views.downvote, name='downvote'),
    path('<int:question_id>/answer_list/', views.answer_list, name='answer_list'),
]
