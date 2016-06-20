# -*- coding: UTF-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from datetime import timedelta
from django.utils import translation

# Create your views here.
def quizList(request):
	quizes = GetQuizList()
	context = {'quizes' : quizes}
	return render(request, 'funnyquiz/quiz_list.html', context)

def quizWelcome(request, quiz_url):
	for quiz in GetQuizList():
		if quiz.QuizUrl == quiz_url:
			cur_quiz = quiz
	return HttpResponse(cur_quiz.QuizName)
	


def GetQuizList():
	q1 = Quiz("Qz001", "你TM真的是多大的么", "true_UofTer", True, "聪明的你，来看看你到底是不是多大的吧", None, True, datetime.now(None))
	q2 = Quiz("Qz002", "你TM根本不是多大的", "fake_UofTer", True, "傻乎乎的你，肯定不是多大的", None, True, datetime.now() + timedelta(minutes = 10))
	return [q1, q2]



class Quiz:
	
	def __init__(self, QuizId, QuizName, QuizUrl, 
				UseStandardWelcomePage, WelcomeMessage, WelcomeImage, 
				UseStandardResultPage, CreatedTime):
		self.QuizId = QuizId
		self.QuizName = QuizName
		self.QuizUrl = QuizUrl
		self.UseStandardWelcomePage = UseStandardWelcomePage
		self.WelcomeMessage = WelcomeMessage
		self.WelcomeImage = WelcomeImage,
		self.UseStandardResultPage = UseStandardResultPage
		self.CreatedTime = CreatedTime
