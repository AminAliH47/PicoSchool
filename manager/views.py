from django.contrib.auth.hashers import make_password
from django.http import (
    HttpResponse,
    JsonResponse,
)
from django.shortcuts import (
    render,
    get_object_or_404,
)
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.views import generic
from account import forms
from account.models import User
from main.decorators import allow_user
from main.mixins import AllowUserMixin
from manager.models import (
    EventCalendar,
    ExternalEventCalendar,
    NoticeBox,
    Major,
    Attendance,
    Assign,
    Classes,
    Books,
    HomeWork,
    EmploymentForm,
)
from manager.filters import (
    StudentFilter,
    ParentFilter,
    TeacherFilter,
)


@allow_user(["is_superuser", "is_manager"])
def manager_panel(request):
    context = {
        "notices": NoticeBox.objects.all().order_by('-publish')[:10],
        "User_count": User.objects.first(),
        "page_title": "پنل مدیریت",
    }
    return render(request, "manager/manager_panel.html", context)


# Calendar Section
@allow_user(["is_superuser", "is_manager"])
def calendar(request):
    context = {
        "page_title": "تقویم رویداد ها",
    }
    return render(request, "manager/calendar.html", context)


@require_POST
@allow_user(['is_superuser', 'is_manager'])
def add_event(request):
    input_value = {
        'id': request.POST.get('id'),
        'title': request.POST.get('title'),
        'start': request.POST.get('start'),
        'backgroundColor': request.POST.get('backgroundColor'),
        'borderColor': request.POST.get('backgroundColor'),
    }

    print(input_value)
    EventCalendar.objects.create(
        id=input_value['id'],
        title=input_value['title'],
        start=input_value['start'],
        backgroundColor=input_value['backgroundColor'],
        borderColor=input_value['borderColor'],
    )
    return HttpResponse(input_value)


@require_POST
@allow_user(['is_superuser', 'is_manager'])
def update_event(request):
    input_value = {
        'id': request.POST.get('id'),
        'start': request.POST.get('start'),
        'end': request.POST.get('end'),
        'description': request.POST.get('description')
    }
    if input_value["start"][10:] == "T00:00:00.000Z":
        start = input_value["start"][:10]
        end = input_value["end"][:10]
    else:
        start = input_value["start"]
        end = input_value["end"]

    print(input_value)

    id = input_value["id"]
    EventCalendar.objects.filter(id=id).update(
        start=start,
        end=end,
    )
    return HttpResponse(input_value)


@require_POST
@allow_user(['is_superuser', 'is_manager'])
def update_event_desc(request):
    input_value = {
        'id': request.POST.get('id'),
        'description': request.POST.get('description')
    }

    print(input_value)
    id = input_value["id"]
    EventCalendar.objects.filter(id=id).update(
        description=input_value['description'],
    )
    return HttpResponse(input_value)


@require_POST
@allow_user(['is_superuser', 'is_manager'])
def delete_event(request):
    input_value = {
        'id': request.POST.get('id'),
    }
    print(input_value)
    EventCalendar.objects.filter(id=input_value['id']).delete()
    return HttpResponse(input_value)


@require_POST
@allow_user(['is_superuser', 'is_manager'])
def add_external_event(request):
    input_value = {
        'id': request.POST.get('id'),
        'title': request.POST.get('title'),
        'backgroundColor': request.POST.get('backgroundColor'),
        'borderColor': request.POST.get('backgroundColor'),
    }

    print(input_value)
    ExternalEventCalendar.objects.create(
        id=input_value['id'],
        title=input_value['title'],
        backgroundColor=input_value['backgroundColor'],
        borderColor=input_value['borderColor'],
    )
    return HttpResponse(input_value)


@require_POST
@allow_user(['is_superuser', 'is_manager'])
def delete_ex_event(request):
    input_value = {
        'id': request.POST.get('id'),
    }
    print(input_value)
    ExternalEventCalendar.objects.filter(id=input_value['id']).delete()
    return HttpResponse(input_value)


@require_POST
@allow_user(['is_superuser', 'is_manager', 'is_teacher'])
def add_notice(request):
    input_value = {
        'writer': request.POST.get('writer'),
        'title': request.POST.get('title'),
        'description': request.POST.get('description'),
    }

    print(input_value)
    if request.user.is_superuser or request.user.is_manager:
        writer_id = input_value['writer']
        writer_id = input_value['writer'] if writer_id else request.user.id
    else:
        writer_id = request.user.id

    NoticeBox.objects.create(
        writer=User.objects.get(id=writer_id),
        title=input_value['title'],
        description=input_value['description'],
    )
    return HttpResponse(input_value)


@require_POST
@allow_user(['is_superuser', 'is_manager'])
def delete_notice(request):
    input_value = {
        'id': request.POST.get('id'),
    }
    print(input_value)
    NoticeBox.objects.filter(id=input_value['id']).delete()
    return HttpResponse(input_value)


@require_POST
@allow_user(['is_superuser', 'is_manager'])
def edit_notice(request):
    input_value = {
        'id': request.POST.get('id'),
        'writer': request.POST.get('writer'),
        'title': request.POST.get('title'),
        'description': request.POST.get('description'),
    }

    print(input_value)

    NoticeBox.objects.filter(id=input_value["id"]).update(
        writer=User.objects.get(id=input_value["writer"]),
        title=input_value['title'],
        description=input_value['description'],
    )
    return HttpResponse(input_value)


# Students Section
@allow_user(['is_superuser', 'is_manager'])
def student_list(request):
    context = {
        'page_title': 'فهرست دانش آموزان',
        'majors': Major.objects.all(),
        'filter': StudentFilter(request.GET, queryset=User.objects.filter(is_active=True, is_student=True)),
    }
    return render(request, "manager/persons/person_list.html", context)


class CreateStudent(AllowUserMixin, generic.CreateView):
    model = User
    form_class = forms.CreateStudentUserForm
    template_name = "manager/persons/person_create.html"
    allowed_users = ["is_superuser", "is_manager"]
    success_url = reverse_lazy("manager:student_list")

    def form_valid(self, form):
        self.obj = form.save(commit=False)
        self.obj.username = form.cleaned_data["national_code"]
        self.obj.password = make_password(form.cleaned_data["password"])
        self.obj.is_student = True
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'ساخت دانش آموز'
        context['majors'] = Major.objects.all()
        return context


class UpdateStudent(AllowUserMixin, generic.UpdateView):
    model = User
    form_class = forms.UpdateStudentUserForm
    context_object_name = "person"
    template_name = "manager/persons/person_create.html"
    allowed_users = ["is_superuser", "is_manager"]
    success_url = reverse_lazy("manager:student_list")

    def form_valid(self, form):
        self.obj = form.save(commit=False)
        self.obj.is_student = True
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'ویرایش دانش آموز'
        context['majors'] = Major.objects.all()
        return context


class DeleteStudent(AllowUserMixin, generic.DeleteView):
    model = User
    context_object_name = "person"
    template_name = "manager/persons/person_delete.html"
    allowed_users = ["is_superuser", "is_manager"]
    success_url = reverse_lazy("manager:student_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "حذف دانش آموز"
        return context


# Parents Section
@allow_user(['is_superuser', 'is_manager'])
def parent_list(request):
    context = {
        'page_title': 'فهرست والدین',
        'filter': ParentFilter(request.GET, queryset=User.objects.filter(is_active=True, is_parent=True)),
    }
    return render(request, "manager/persons/person_list.html", context)


class CreateParent(AllowUserMixin, generic.CreateView):
    model = User
    form_class = forms.CreateParentUserForm
    template_name = "manager/persons/person_create.html"
    allowed_users = ["is_superuser", "is_manager"]
    success_url = reverse_lazy("manager:parent_list")

    def form_valid(self, form):
        self.obj = form.save(commit=False)
        self.obj.username = form.cleaned_data["national_code"]
        self.obj.password = make_password(form.cleaned_data["password"])
        self.obj.is_parent = True
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'ساخت والدین'
        return context


class UpdateParent(AllowUserMixin, generic.UpdateView):
    model = User
    form_class = forms.UpdateParentUserForm
    context_object_name = "person"
    template_name = "manager/persons/person_create.html"
    allowed_users = ["is_superuser", "is_manager"]
    success_url = reverse_lazy("manager:parent_list")

    def form_valid(self, form):
        self.obj = form.save(commit=False)
        self.obj.is_parent = True
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'ویرایش والدین'
        return context


class DeleteParent(AllowUserMixin, generic.DeleteView):
    model = User
    context_object_name = "person"
    template_name = "manager/persons/person_delete.html"
    allowed_users = ["is_superuser", "is_manager"]
    success_url = reverse_lazy("manager:parent_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "حذف والد"
        return context


# Teacher Section
@allow_user(['is_superuser', 'is_manager'])
def teacher_list(request):
    context = {
        'page_title': 'فهرست دبیران',
        'filter': TeacherFilter(request.GET, queryset=User.objects.filter(is_active=True, is_teacher=True)),
    }
    return render(request, "manager/persons/person_list.html", context)


class CreateTeacher(AllowUserMixin, generic.CreateView):
    model = User
    form_class = forms.CreateTeacherUserForm
    template_name = "manager/persons/person_create.html"
    allowed_users = ["is_superuser", "is_manager"]
    success_url = reverse_lazy("manager:teacher_list")

    def form_valid(self, form):
        self.obj = form.save(commit=False)
        self.obj.username = form.cleaned_data["national_code"]
        self.obj.password = make_password(form.cleaned_data["password"])
        self.obj.is_teacher = True
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'ساخت دبیر'
        return context


class UpdateTeacher(AllowUserMixin, generic.UpdateView):
    model = User
    form_class = forms.UpdateTeacherUserForm
    context_object_name = "person"
    template_name = "manager/persons/person_create.html"
    allowed_users = ["is_superuser", "is_manager"]
    success_url = reverse_lazy("manager:teacher_list")

    def form_valid(self, form):
        self.obj = form.save(commit=False)
        self.obj.is_teacher = True
        single_or_married = form.cleaned_data['single_or_married']
        if single_or_married == "مجرد":
            self.obj.spouse_fullname = ""
            self.obj.spouse_phone = ""
            self.obj.child_num = None
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'ویرایش دبیر'
        return context


class DeleteTeacher(AllowUserMixin, generic.DeleteView):
    model = User
    context_object_name = "person"
    template_name = "manager/persons/person_delete.html"
    allowed_users = ["is_superuser", "is_manager"]
    success_url = reverse_lazy("manager:teacher_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "حذف والد"
        return context


@allow_user(['is_superuser', 'is_manager'])
def password_change(request, pk):
    user = get_object_or_404(User, pk=pk)

    if request.method == "POST":
        input_value = {
            "password1": request.POST.get("password1"),
            "password2": request.POST.get("password2"),
        }
        password1 = input_value['password1']
        password2 = input_value['password2']

        if password1 == password2:
            user.password = make_password(password1)
            user.save()
        else:
            return JsonResponse({"error": True, "message": "گذرواژه ها مغایرت دارند"})

    context = {
        "page_title": "تغییر گذرواژه",
        "user_p": user,
    }
    return render(request, "manager/persons/change_password.html", context)


@require_POST
@allow_user(['is_superuser', 'is_manager', 'is_teacher'])
def change_att_status(request):
    """
    change attendance status
    """
    input_value = {
        'ass_id': request.POST.get('ass_id'),
        'status': request.POST.get('status'),
    }

    print(input_value)
    Assign.objects.filter(id=input_value['ass_id']).update(attendance_status=input_value['status'])
    return HttpResponse(input_value)


@require_POST
@allow_user(['is_superuser', 'is_manager', 'is_teacher'])
def add_att_status(request):  # add attendance status for student
    input_value = {
        'att_id': request.POST.get('att_id'),
        'stu_id': request.POST.get('stu_id'),
        'status': request.POST.get('status'),
    }

    print(input_value)
    assign_obj = Assign(
        attendance=Attendance.objects.get(id=input_value['att_id']),
        attendance_status=input_value['status'],
        student=User.objects.get(id=input_value['stu_id'])
    )
    assign_obj.save()
    return HttpResponse(input_value)


@require_POST
@allow_user(['is_superuser', 'is_manager', 'is_teacher'])
def change_att_note(request):  # change attendance note for student
    input_value = {
        'ass_id': request.POST.get('ass_id'),
        'note': request.POST.get('note'),
    }

    print(input_value)

    Assign.objects.filter(id=input_value['ass_id']).update(attendance_note=input_value['note'])
    return HttpResponse(input_value)


@require_POST
@allow_user(['is_superuser', 'is_manager'])
def create_att(request):  # create attendance for a class
    input_value = {
        'book_id': request.POST.get('book_id'),
        'class_id': request.POST.get('class_id'),
    }

    print(input_value)
    attendance_obj = Attendance(
        attendance_class=Classes.objects.get(id=input_value['class_id']),
        book=Books.objects.get(id=input_value['book_id'])
    )
    attendance_obj.save()
    return HttpResponse(input_value)


@allow_user(['is_superuser', 'is_manager'])
def report_card(request):
    context = {
        'page_title': 'ساخت کارنامه',
        'students': User.objects.filter(is_active=True, is_student=True),
        'books': Books.objects.filter()
    }
    return render(request, "manager/report_card/report_card.html", context)


def create_report_card(request):
    context = {}
    return HttpResponse()


@require_POST
@allow_user(['is_superuser', 'is_manager', 'is_teacher'])
def create_hw(request):  # create homework for attendance
    input_value = {
        'hw_title': request.POST.get('hw_title'),
        'hw_description': request.POST.get('hw_description'),
        'hw_att': request.POST.get('hw_att'),
    }

    print(input_value)
    homework_obj = HomeWork(
        attendance=Attendance.objects.get(id=input_value['hw_att']),
        title=input_value['hw_title'], description=input_value['hw_description']
    )
    homework_obj.save()
    return HttpResponse(input_value)


@require_POST
@allow_user(['is_superuser', 'is_manager', 'is_teacher'])
def upload_emp_form(request):  # Upload Image Form for employment form
    image_value = request.FILES.get('file')
    input_value = request.POST.get('emp_form_id')
    obj = EmploymentForm.objects.get(id=input_value)
    obj.form_image = image_value
    obj.save()
    return HttpResponse(input_value)
