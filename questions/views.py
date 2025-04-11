from django.shortcuts import render, redirect, get_object_or_404
from .models import Question
from .forms import QuestionForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.utils.text import slugify
import random
import string
from answers.forms import AnswerForm

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
