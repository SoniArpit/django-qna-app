from django import forms
from .models import Question

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'body']

    
    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'class': 'input w-full mb-4 mt-2',
            'placeholder': 'Enter your question title here'
        })
        # for body class is 'textarea w-full mb-4 mt-2'
        self.fields['body'].widget.attrs.update({
            'class': 'textarea w-full mb-4 mt-2',
            'placeholder': 'Explain your question in detail'
        })