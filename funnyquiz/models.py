from django.db import models


# Create your models here.
class Quiz(models.Model):
    QuizName = models.CharField(max_length=50)
    QuizUrl = models.CharField(max_length=200)
    UseStandardWelcomePage = models.BooleanField(default=True)
    WelcomeMessage = models.CharField(max_length=200)
    WelcomeImage = models.FileField(null=True, blank=True)
    UseStandardResultPage = models.BooleanField(default=True)
    CreatedTime = models.DateField()

    def __str__(self):
        return str(self.pk) + ' - ' + str(self.QuizName)


class Question(models.Model):
    Quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    QuestionText = models.CharField(max_length=200)
    '''QuestionHasImage = models.BooleanField(default=False)'''
    QuestionImage = models.FileField(null=True, blank=True)
    

    def __str__(self):
        return str(self.pk) + ' - ' + self.QuestionText


class Answer(models.Model):
    ParentQuestion = models.ForeignKey(Question, on_delete=models.CASCADE)
    AnswerText = models.CharField(max_length=100)
    AnswerImg = models.FileField(null=True, blank=True)
    '''AnswerHasImage = models.BooleanField(default=False)'''
    IsCorrectAnswer = models.BooleanField(default=False)

    def __str__(self):
        return self.AnswerText

class Quizstate(models.Model):
    Quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    VisitorCount = models.IntegerField()
    CompletionCount = models.IntegerField()
    AvgCorrecteness = models.FloatField()
    StdDev = models.FloatField()



