from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST
from account.models import User
from main.decorators import allow_user
from manager.models import (
    NoticeBox,
    Major,
    EmploymentForm,
    Assign,
)
from quiz.models import QuizResult


@allow_user(["is_superuser", "is_manager", "is_student"])
def student_view(request):
    def all_status_func():
        all_status = Assign.objects.filter(student=request.user).aggregate(count=Count('id'))
        count_all = 0
        if all_status["count"] is not None:
            count_all = int(all_status["count"])
        return count_all

    def present_percent():
        present = Assign.objects.filter(student=request.user, attendance_status='حاضر').aggregate(count=Count('id'))
        count_present = 0
        if present["count"] is not None:
            count_present = int(present["count"])
        try:
            result = round((count_present / all_status_func()) * 100, 0)
        except ZeroDivisionError:
            result = 0
        return result

    def absent_percent():
        absent = Assign.objects.filter(student=request.user, attendance_status='غایب').aggregate(count=Count('id'))
        count_present = 0
        if absent["count"] is not None:
            count_present = int(absent["count"])
        try:
            result = round((count_present / all_status_func()) * 100, 0)
        except ZeroDivisionError:
            result = 0
        return result

    def plate_percent():
        plate = Assign.objects.filter(student=request.user, attendance_status='حاضر (با تاخیر)').aggregate(
            count=Count('id'))
        count_present = 0
        if plate["count"] is not None:
            count_present = int(plate["count"])
        try:
            result = round((count_present / all_status_func()) * 100, 0)
        except ZeroDivisionError:
            result = 0
        return result

    context = {
        "notices": NoticeBox.objects.all().order_by('-publish')[:10],
        "page_title": "پنل دانش آموزان",
        'majors': Major.objects.all(),
        'present': present_percent(),
        'absent': absent_percent(),
        'plate': plate_percent(),
        'results': QuizResult.objects.filter(user=request.user),
    }
    return render(request, "student/student_panel.html", context)


@require_POST
@allow_user(['is_superuser', 'is_manager', 'is_student'])
def create_emp_form(request):  # add employment form status
    input_value = {
        'stu_id': request.POST.get('stu_id'),
        'organ': request.POST.get('organ'),
    }

    print(input_value)
    emp_form = EmploymentForm(student=User.objects.get(id=input_value['stu_id']),
                              organ=input_value['organ'])
    emp_form.save()
    return HttpResponse(input_value)
