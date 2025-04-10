from django.db import models
from questions.models import Question
from django.contrib.auth.models import User

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answers')
    like_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Answer by {self.author} to {self.question}'


# answer likes
class AnswerLike(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='liked_answers')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('answer', 'user')

    def __str__(self):
        return f'Like by {self.user} for {self.answer}'