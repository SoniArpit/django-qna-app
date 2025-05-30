from django.shortcuts import render, redirect, get_object_or_404
from .models import Question
from .forms import QuestionForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.utils.text import slugify
import random
import string
from answers.forms import AnswerForm
from answers.models import AnswerLike
from django.db import models
from django.db.models import Exists, OuterRef

@login_required
def ask_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            random_alphanumeric = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
            question.slug = slugify(form.cleaned_data['title']) + '-' + random_alphanumeric
            question.save()
            # redirect to the question detail page after saving
            return redirect(question.get_absolute_url())
    else:
        form = QuestionForm()
    return render(request, 'questions/ask_question.html', {'form': form})

def question_list(request):
    questions = Question.objects.all().order_by('-created_at')
    page = request.GET.get('page', 1)
    paginator = Paginator(questions, 10)  # Show 10 questions per page
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)
    
    return render(request, 'questions/question_list.html', {'questions': questions})

def question_detail(request, slug):
    question = get_object_or_404(Question, slug=slug)
    answer_form = AnswerForm()
    answers = question.answers.all().order_by('-created_at')
    # Annotate each answer with whether the current user has liked it
    if request.user.is_authenticated:
        likes_subquery = AnswerLike.objects.filter(
            user = request.user,
            answer = OuterRef('pk')
        )
        answers = answers.annotate(
            has_liked=Exists(likes_subquery)
        )
    else:
        answers = answers.annotate(
           has_liked=models.Value(False, output_field=models.BooleanField())
        )

    # paginator for answers
    page = request.GET.get('page', 1)
    paginator = Paginator(answers, 10)  # Show 10 answers per page
    try:
        answers = paginator.page(page)
    except PageNotAnInteger:
        answers = paginator.page(1)
    except EmptyPage:
        answers = paginator.page(paginator.num_pages)
    return render(request, 'questions/question_detail.html', {'question': question, 'answer_form': answer_form, 'answers': answers})


@login_required
def edit_question(request, slug):
    question = get_object_or_404(Question, slug=slug)
    if request.user != question.author:
        return redirect('questions:question_detail', slug=slug)
    
    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.slug = slugify(form.cleaned_data['title'])
            question.save()
            return redirect(question.get_absolute_url())
    else:
        form = QuestionForm(instance=question)
    return render(request, 'questions/edit_question.html', {'form': form, 'question': question})


@login_required
def delete_question(request, slug):
    question = get_object_or_404(Question, slug=slug)
    if request.user == question.author:
        question.delete()
        return redirect('questions:home')
    else:
        return redirect('questions:question_detail', slug=slug)