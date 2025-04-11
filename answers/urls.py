from django.urls import path
from . import views

app_name = 'answers'
urlpatterns = [
    path('<slug:question_id>/answer/', views.answer_question, name='answer_question'),
]