from django.http import Http404
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy

from account.models import User
from manager.models import Classes, Attendance, HomeWork, EmploymentForm
from quiz.models import Quiz


def allow_user(user_permission_list):
    def decorator(view_func):
        def inner(request, *args, **kwargs):
            user = []
            if request.user.is_anonymous:
                user.append("is_anonymous")
            elif request.user.is_superuser or request.user.is_manager:
                user.extend(["is_superuser", "is_manager"])
            elif request.user.is_parent:
                user.append("is_parent")
            elif request.user.is_teacher:
                user.append("is_teacher")
            elif request.user.is_student:
                user.append("is_student")

            if user[0] not in user_permission_list:
                return redirect(reverse_lazy('main:login'))
            else:
                return view_func(request, *args, **kwargs)

        return inner

    return decorator


def allow_class_teacher():
    def decorator(view_func):
        def inner(request, *args, **kwargs):
            classes = get_object_or_404(Classes, pk=kwargs.get('pk'))
            if request.user.is_superuser or request.user.is_manager:
                return view_func(request, *args, **kwargs)
            elif request.user.pk in classes.teacher.values_list('pk', flat=True):
                return view_func(request, *args, **kwargs)
            else:
                raise Http404()

        return inner

    return decorator


def allow_att_teacher():
    def decorator(view_func):
        def inner(request, *args, **kwargs):
            att = get_object_or_404(Attendance, pk=kwargs.get('pk'))
            if request.user.is_superuser or request.user.is_manager:
                return view_func(request, *args, **kwargs)
            elif request.user.pk in att.attendance_class.teacher.values_list('pk', flat=True):
                return view_func(request, *args, **kwargs)
            else:
                raise Http404()

        return inner

    return decorator


def allow_hw_student():
    def decorator(view_func):
        def inner(request, *args, **kwargs):
            hw = get_object_or_404(HomeWork, pk=kwargs.get('pk'))
            if request.user.is_superuser or request.user.is_manager:
                return view_func(request, *args, **kwargs)
            elif hw.attendance.attendance_class == request.user.student_class:
                return view_func(request, *args, **kwargs)
            else:
                raise Http404()

        return inner

    return decorator


def allow_emp_form_student():
    def decorator(view_func):
        def inner(request, *args, **kwargs):
            emp_form = get_object_or_404(EmploymentForm, pk=kwargs.get('pk'))
            if request.user.is_superuser or request.user.is_manager:
                return view_func(request, *args, **kwargs)
            elif emp_form.student.pk == request.user.pk:
                return view_func(request, *args, **kwargs)
            else:
                raise Http404()

        return inner

    return decorator


def parent_access():
    def decorator(view_func):
        def inner(request, *args, **kwargs):
            student = get_object_or_404(User, pk=kwargs.get('pk'))
            if student.parent == request.user or request.user.is_superuser or request.user.is_manager or \
                    student.pk == request.user.pk:
                return view_func(request, *args, **kwargs)
            else:
                raise Http404()

        return inner

    return decorator


def student_access():
    def decorator(view_func):
        def inner(request, *args, **kwargs):
            parent = get_object_or_404(User, pk=kwargs.get('pk'))
            if request.user.is_superuser or request.user.is_manager or parent.pk == request.user.pk:
                return view_func(request, *args, **kwargs)
            else:
                raise Http404()

        return inner

    return decorator


def quiz_access():
    def decorator(view_func):
        def inner(request, *args, **kwargs):
            last_url = request.META.get("HTTP_REFERER")
            if last_url:
                return view_func(request, *args, **kwargs)
            else:
                raise Http404()

        return inner

    return decorator
