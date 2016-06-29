from django.db import models


# Create your models here.
class Quiz(models.Model):
    QuizName = models.CharField(max_length=50)
    UseStandardWelcomePage = models.BooleanField(default=True)
    WelcomeMessage = models.CharField(max_length=200)
    WelcomeImage = models.FileField()
    UseStandardResultPage = models.BooleanField(default=True)

    def __str__(self):
        return self.pk + ' - ' + self.QuizName


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    QuestionText = models.CharField(max_length=200)
    HasImage = models.BooleanField(default=False)
    QuestionImage = models.FileField()
    CorrectAnswer = models.CharField(max_length=100)
    Answer2 = models.CharField(max_length=100)
    Answer3 = models.CharField(max_length=100)
    Answer4 = models.CharField(max_length=100)

    def __str__(self):
        return self.pk + ' - ' + self.QuestionText


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    AnswerText = models.CharField(max_length=100)
    AnswerImg = models.FileField()

    def __str__(self):
        return self.AnswerText



