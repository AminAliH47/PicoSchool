from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy


def is_login():
    def decorator(view_func):
        def wrap(request, *args, **kwargs):
            if request.user.is_anonymous:
                return view_func(request, *args, **kwargs)
            if request.user.is_superuser or request.user.is_manager:
                return redirect(reverse_lazy('manager:manager_panel'))
            elif request.user.is_teacher:
                return redirect(reverse_lazy('teacher:teacher_panel'))
            elif request.user.is_parent:
                return redirect(reverse_lazy('parent:parent_panel'))
            elif request.user.is_student:
                return redirect(reverse_lazy('student:student_panel'))

        return wrap

    return decorator
