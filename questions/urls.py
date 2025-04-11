from django.urls import path
from . import views

app_name = 'questions'
urlpatterns = [
    path('', views.question_list, name='home'),
    path('ask/', views.ask_question, name='ask_question'),
    path('<str:slug>/', views.question_detail, name='question_detail'),
    path('<str:slug>/edit/', views.edit_question, name='edit_question'),
    path('<str:slug>/delete/', views.delete_question, name='delete_question'),
]
