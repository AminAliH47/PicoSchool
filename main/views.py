import jdatetime
import feedparser
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.http import Http404
from django.shortcuts import (
    render,
    get_object_or_404, redirect,
)
from django.urls import reverse_lazy
from django.utils import timezone
from extensions.utils import change_month
from account.models import User
from main.decorators import (
    allow_user,
    allow_class_teacher,
    allow_att_teacher,
    allow_hw_student,
    allow_emp_form_student,
    parent_access,
    student_access,
)
from manager.filters import (
    ClassFilter,
    EMPFormFilter,
)
from manager.models import (
    NoticeBox,
    Major,
    Attendance,
    Classes,
    Books,
    HomeWork,
    EmploymentForm,
    Assign,
)


def index(request):
    if request.user.is_anonymous:
        return redirect(reverse_lazy("account:login"))
    if request.user.is_superuser or request.user.is_manager:
        return redirect(reverse_lazy('manager:manager_panel'))
    elif request.user.is_teacher:
        return redirect(reverse_lazy('teacher:teacher_panel'))
    elif request.user.is_parent:
        return redirect(reverse_lazy('parent:parent_panel'))
    elif request.user.is_student:
        return redirect(reverse_lazy('student:student_panel'))


@login_required()
def events(request):
    context = {
        "page_title": "رویداد ها",
        "notices": NoticeBox.objects.all()
    }
    return render(request, "main/events.html", context)


@login_required()
def notice_box(request):
    context = {
        "page_title": "اعلانات",
        "notices": NoticeBox.objects.all().order_by('-publish')
    }
    return render(request, "main/notice_box.html", context)


@parent_access()
@allow_user(['is_superuser', 'is_manager', 'is_parent', 'is_student'])
def student_detail(request, pk):
    def all_status_func():
        all_status = Assign.objects.filter(student=pk).aggregate(count=Count('id'))
        count_all = 0
        if all_status["count"] is not None:
            count_all = int(all_status["count"])
        return count_all

    def present_percent():
        present = Assign.objects.filter(student=pk, attendance_status='حاضر').aggregate(count=Count('id'))
        count_present = 0
        if present["count"] is not None:
            count_present = int(present["count"])
        result = round((count_present / all_status_func()) * 100, 0)
        return result

    def absent_percent():
        absent = Assign.objects.filter(student=pk, attendance_status='غایب').aggregate(count=Count('id'))
        count_present = 0
        if absent["count"] is not None:
            count_present = int(absent["count"])
        result = round((count_present / all_status_func()) * 100, 0)
        return result

    def plate_percent():
        plate = Assign.objects.filter(student=pk, attendance_status='حاضر (با تاخیر)').aggregate(
            count=Count('id'))
        count_present = 0
        if plate["count"] is not None:
            count_present = int(plate["count"])
        result = round((count_present / all_status_func()) * 100, 0)
        return result

    user = User.objects.filter(is_active=True, is_student=True)
    context = {
        'person': get_object_or_404(user, pk=pk),
        'page_title': 'جزئیات دانش آموز',
        'majors': Major.objects.all(),
        'present': present_percent(),
        'absent': absent_percent(),
        'plate': plate_percent(),
    }
    return render(request, "main/persons/person_detail.html", context)


@student_access()
@allow_user(['is_superuser', 'is_manager', 'is_parent'])
def parent_detail(request, pk):
    user = User.objects.filter(is_active=True, is_parent=True)
    context = {
        'person': get_object_or_404(user, pk=pk),
        'page_title': 'جزئیات والد یا قیم',
    }
    return render(request, "main/persons/person_detail.html", context)


@student_access()
@allow_user(['is_superuser', 'is_manager', 'is_teacher'])
def teacher_detail(request, pk):
    user = User.objects.filter(is_active=True, is_teacher=True)
    context = {
        'person': get_object_or_404(user, pk=pk),
        'page_title': 'جزئیات دبیر',
    }
    return render(request, "main/persons/person_detail.html", context)


@allow_user(['is_superuser', 'is_manager', 'is_teacher'])
def class_list(request):
    context = {
        'page_title': "لیست کلاس ها",
        'majors': Major.objects.all(),
    }
    if request.user.is_superuser or request.user.is_manager:
        context['filter'] = ClassFilter(request.GET, queryset=Classes.objects.all())
    elif request.user.is_teacher:
        context['filter'] = ClassFilter(request.GET, queryset=Classes.objects.filter(teacher__pk=request.user.pk))
    else:
        raise Http404()
    return render(request, "main/classes/class_list.html", context)


@allow_class_teacher()
@allow_user(['is_superuser', 'is_manager', 'is_teacher'])
def class_detail(request, pk):
    cls = get_object_or_404(Classes, pk=pk)
    context = {
        "class": cls,
        "page_title": "جزئیات کلاس",
        'atts': Classes.objects.filter(pk=pk, attendance_class__pk=pk),
        'jalali_date': change_month(str(jdatetime.date.fromgregorian(date=timezone.now()))),
        'books': Books.objects.filter(grade__pk=cls.grade.pk, major__pk=cls.major.pk),
    }
    return render(request, "main/classes/class_detail.html", context)


@allow_att_teacher()
@allow_user(['is_superuser', 'is_manager', 'is_teacher'])
def attendance_detail(request, pk, date):
    context = {
        "attendance": get_object_or_404(Attendance, pk=pk, date=date),
        "page_title": "جزئیات حضور و غیاب",
    }
    return render(request, "main/classes/class_detail.html", context)


@allow_user(['is_superuser', 'is_manager', 'is_teacher', 'is_student'])
def home_work_list(request):
    context = {
        'page_title': 'لیست تکالیف',
    }
    if request.user.is_superuser or request.user.is_manager:
        context['home_works'] = HomeWork.objects.all()
    elif request.user.is_student:
        context['home_works'] = HomeWork.objects.filter(attendance__attendance_class=request.user.student_class)
    elif request.user.is_teacher:
        context['home_works'] = HomeWork.objects.filter(attendance__attendance_class__teacher__pk=request.user.pk)
    return render(request, 'main/classes/class_list.html', context)


@allow_hw_student()
@allow_user(['is_superuser', 'is_manager', 'is_teacher', 'is_student'])
def home_work_detail(request, pk):
    context = {
        'page_title': 'جزئیات تکلیف',
        'home_work': get_object_or_404(HomeWork, pk=pk)
    }
    return render(request, 'main/classes/class_detail.html', context)


@allow_user(['is_superuser', 'is_manager', 'is_student'])
def employment_form_list(request):
    context = {
        "page_title": "لیست فرم های اشتغال به تحصیل",
    }
    if request.user.is_superuser or request.user.is_manager:
        context['filter'] = EMPFormFilter(request.GET, queryset=EmploymentForm.objects.all())
    elif request.user.is_student:
        context['filter'] = EMPFormFilter(request.GET,
                                          queryset=EmploymentForm.objects.filter(student__pk=request.user.pk))
    return render(request, 'main/classes/class_list.html', context)


@allow_emp_form_student()
@allow_user(['is_superuser', 'is_manager', 'is_student'])
def employment_form_detail(request, pk):
    context = {
        'page_title': 'جزئیات فرم',
        'employment_form': get_object_or_404(EmploymentForm, pk=pk)
    }
    if request.method == "POST":
        if request.is_ajax:
            input_value = {
                'status': request.POST.get('status'),
                'emp_form_id': request.POST.get('emp_form_id'),
            }
            print(input_value)
            EmploymentForm.objects.filter(id=input_value['emp_form_id']).update(status=input_value['status'])

    return render(request, 'main/classes/class_detail.html', context)


@login_required()
def news_list(request):
    feeds = feedparser.parse('https://www.mehrnews.com/rss/tp/68')
    context = {
        'feeds': feeds,
        'page_title': 'اخبار آموزش و پرورش'
    }
    return render(request, "main/news_list.html", context)
