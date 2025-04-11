from django.shortcuts import render, redirect
from questions.models import Question
from .forms import AnswerForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import Answer, AnswerLike
from django.http import JsonResponse

@login_required
def answer_question_view(request, question_id):
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


@login_required 
def like_answer(request, answer_id):
    answer = get_object_or_404(Answer, id=answer_id)
    user = request.user
    liked = False
    # Check if the user has already liked this answer
    existing_like = AnswerLike.objects.filter(answer=answer, user=user).first()
    if existing_like:
        # User has already liked the answer, so we remove the like
        existing_like.delete()
        answer.like_count -= 1
        answer.save()
    else:
        # User has not liked the answer yet, so we create a new like
        AnswerLike.objects.create(answer=answer, user=user)
        answer.like_count += 1
        answer.save()
        liked = True
    
    return JsonResponse({
        "like_count": answer.like_count,
        "has_liked": liked,
    })