from django import forms
from .models import Answer

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['body']
    
    def __init__(self, *args, **kwargs):
        super(AnswerForm, self).__init__(*args, **kwargs)
        self.fields['body'].widget.attrs.update({
            'class': 'textarea w-full mb-4 mt-2',
            'placeholder': 'Explain your question in detail'
        })