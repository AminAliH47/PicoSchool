from django.contrib import admin
from quiz import models


class QuizAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'topic', 'show_quiz', 'quiz_class', 'difficulty')


admin.site.register(models.Quiz, QuizAdmin)


class QuizMultipleAnswersInline(admin.TabularInline):
    model = models.QuizMultipleAnswers


class QuizMultipleAnswersAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'get_question',)

    def get_question(self, obj):
        return obj.question

    get_question.short_description = "برای سوال"
    get_question.allow_tags = True


admin.site.register(models.QuizMultipleAnswers, QuizMultipleAnswersAdmin)
admin.site.register(models.QuizDescAnswers)


class QuizQuestionAdmin(admin.ModelAdmin):
    inlines = (QuizMultipleAnswersInline,)


admin.site.register(models.QuizQuestion, QuizQuestionAdmin)


class QuizResultAdmin(admin.ModelAdmin):
    list_display = ('user', 'quiz',)
    # readonly_fields = ('score',)


admin.site.register(models.QuizResult, QuizResultAdmin)
