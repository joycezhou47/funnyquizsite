# -*- coding: UTF-8 -*-

import pdb; pdb.set_trace()

from .models import *
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from datetime import datetime
from datetime import timedelta
from django.utils import translation

import random;


# Create your views here.
def quizList(request):
    quizes = Quiz.objects.all()
    context = {'quizes' : quizes}
    return render(request, 'funnyquiz/quiz_list.html', context)


def quizWelcome(request, quiz_url):
    #for quiz in GetQuizList():
    #    if quiz.QuizUrl == quiz_url:
    #        cur_quiz = quiz
    cur_quiz = get_object_or_404(Quiz, QuizUrl=quiz_url)
    if request.method == 'GET':
        time_clicked_str = request.COOKIES.get('clicked')
        print(time_clicked_str)
        time_clicked = 0
        time_clicked_str = request.COOKIES.get('clicked')
    elif request.method == 'POST':
        time_clicked_str = request.COOKIES.get('clicked')
        time_clicked = int(time_clicked_str)
        answer_id_selected = request.POST.get("answer", "")
        answer_selected = get_object_or_404(Answer, pk=int(answer_id_selected))
        if (answer_selected.IsCorrectAnswer):
            time_clicked += 1
        '''correct_answer = random.choice(("answer1", "answer2", "answer3", "answer4"))
        if request.POST.get(correct_answer, ""):
            time_clicked += 1'''
    '''request.session['clicked'] = time_clicked'''
    next_question = random.choice(cur_quiz.question_set.all())
    
    context = {'cur_quiz' : cur_quiz, 'time_clicked' : time_clicked, 'this_question': next_question}
    response = render(request, 'funnyquiz/quiz_welcome.html', context)
    response.set_cookie('clicked', time_clicked)
    return response


def quizResult(request, quiz_url):
    cur_quiz = get_object_or_404(Quiz, QuizUrl=quiz_url)
    cur_quizstate = cur_quiz.quizstate_set.filter(id=1)
    context = {'cur_quiz' : cur_quiz, 'cur_quizstate' : cur_quizstate}
    response = render(request, 'funnyquiz/quiz_result.html', context)
    return response


'''def GetQuizList():
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
'''
