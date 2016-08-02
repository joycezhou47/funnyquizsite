from django.contrib import admin
from .models import Quiz, Question, Answer, Quizstate
# Register your models here.
admin.site.register(Quizstate)


class QuestionInline(admin.TabularInline):
    model = Question


class AnswerInline(admin.TabularInline):
    model = Answer


class QuizstateInline(admin.TabularInline):
    model = Quizstate


class AnswerAdmin(admin.ModelAdmin):
    fields = ['AnswerText', 'AnswerImg', 'IsCorrectAnswer']
    list_display = ['AnswerText', 'ParentQuestion',
                    'IsCorrectAnswer']
    list_filter = ['IsCorrectAnswer', 'ParentQuestion']
    search_fields = ['AnswerText']

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]
    list_filter = ['Quiz']
    fields = ['QuestionText', 'QuestionImage']
    list_display = ['QuestionText', 'Quiz']
    search_fields = ['QuestionText']

class QuizAdmin(admin.ModelAdmin):
    # The first element of each tuple in fieldsets is the
    # title of the field.
    fieldsets = [
        ('Quiz Information', {
            'fields': ['QuizName', 'QuizUrl', 'WelcomeMessage',
                       ],
        }),
        # pub_date = models.DateTimeField('date published')
        ('If Standard', {
            'fields': ['UseStandardWelcomePage',
                       'UseStandardResultPage',],
        }),
        ('Image', {
            'fields': ['WelcomeImage',],
        }),
        ('Time', {
            'fields': ['CreatedTime',],
        }),
    ]
    inlines = [QuestionInline, QuizstateInline]
    list_display = ['QuizName', 'QuizUrl',
                    'UseStandardWelcomePage',
                    'UseStandardResultPage']
    search_fields = ['QuizName']


admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
