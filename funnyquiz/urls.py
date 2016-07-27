from django.conf.urls import url

from . import views

app_name = 'funnyquiz'
urlpatterns = [
	url(r'^$', views.quizList, name='quiz_index'),
	url(r'^(?P<quiz_url>[^/]+)/$', views.quizWelcome, name='quiz_welcome'),
    url(r'^(?P<quiz_url>[^/]+)/result/$', views.quizResult,
		name='quiz_result'),
]
