from django.urls import path
from . import views

app_name = 'answers'
urlpatterns = [
    path('<slug:question_id>/answer/', views.answer_question, name='answer_question'),
    path('like/<int:answer_id>/', views.like_answer, name='like_answer'),
    path('edit/<int:answer_id>/', views.edit_answer, name='edit_answer'),
    path('delete/<int:answer_id>/', views.delete_answer, name='delete_answer'),
]