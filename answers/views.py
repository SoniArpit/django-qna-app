from django.shortcuts import render, redirect
from questions.models import Question
from .forms import AnswerForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def answer_question(request, question_id):
    question = Question.objects.get(id=question_id)
    
    # redirect to the question detail page after saving
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.author = request.user
            answer.save()
    
    return redirect(question.get_absolute_url())