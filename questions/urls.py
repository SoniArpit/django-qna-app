from django.urls import path
from . import views

app_name = 'questions'
urlpatterns = [
    path('', views.question_list, name='home'),
    path('ask/', views.ask_question, name='ask_question'),
    path('<str:slug>/', views.question_detail, name='question_detail'),
]
