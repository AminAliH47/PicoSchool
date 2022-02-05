from django.db.models import Count
from django.shortcuts import render
from account.models import User
from main.decorators import allow_user
from manager.filters import ClassFilter
from manager.models import (
    NoticeBox,
    Classes,
    Major,
)
from quiz.models import Quiz


@allow_user(["is_superuser", "is_manager", "is_teacher"])
def teacher_view(request):
    def all_count():
        reviews = Quiz.objects.filter(quiz_class__teacher__pk=request.user.pk).aggregate(count=Count('id'))
        count = 0
        if reviews["count"] is not None:
            count = int(reviews["count"])
        return count

    context = {
        "notices": NoticeBox.objects.all().order_by('-publish')[:4],
        "filter": ClassFilter(request.GET, queryset=Classes.objects.filter(teacher__pk=request.user.pk)),
        "majors": Major.objects.all(),
        "User_count": User.objects.first(),
        "Quiz_count": all_count(),
        "page_title": "پنل دبیران"
    }
    return render(request, "teacher/teacher_panel.html", context)
