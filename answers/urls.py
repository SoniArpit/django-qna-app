from django.urls import path
from . import views

app_name = 'answers'
urlpatterns = [
    path('<slug:question_id>/answer/', views.answer_question_view, name='answer_question'),
    path('like/<int:answer_id>/', views.like_answer, name='like_answer'),
]