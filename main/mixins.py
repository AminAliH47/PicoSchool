from django.http import Http404
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy

from account.models import User
from main.decorators import allow_user


class AllowUserMixin:
    def dispatch(self, request, *args, **kwargs):
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

        if user[0] not in self.allowed_users:
            return redirect(reverse_lazy('main:login'))
        else:
            return super().dispatch(request, *args, **kwargs)


class UserRoleMixin:
    def form_valid(self, form):
        if self.request.resolver_match.url_name == "student_create":
            self.obj = form.save(commit=False)
            self.obj.is_student = True
        return super().form_valid(form)


class ParentAccessMixin:
    def dispatch(self, request, pk, *args, **kwargs):
        student = get_object_or_404(User, pk=pk)
        if student.parent == request.user or request.user.is_superuser or request.user.is_manager or \
                student.pk == request.user.pk:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404()


class StudentAccessMixin:
    def dispatch(self, request, pk, *args, **kwargs):
        parent = get_object_or_404(User, pk=pk)
        if request.user.is_superuser or request.user.is_manager or parent.pk == request.user.pk:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404()
