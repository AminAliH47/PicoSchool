import django_filters as filters
from django.db.models import Value, Q
from django.db.models.functions import Concat
from django.forms import TextInput

from account.models import User
from manager.models import Classes, EmploymentForm
from quiz.models import Quiz


class StudentFilter(filters.FilterSet):
    full_name = filters.CharFilter(method='fullname_filter', lookup_expr='icontains',
                                   widget=TextInput(attrs={'placeholder': 'جستجو ...'}))

    def fullname_filter(self, queryset, name, value):
        queryset = User.objects.filter(is_active=True, is_student=True).annotate(
            fullname=Concat('first_name', Value(' '), 'last_name'))
        return queryset.filter(Q(fullname__icontains=value))

    class Meta:
        model = User
        fields = ('grade', 'major', 'full_name')


class ParentFilter(filters.FilterSet):
    full_name = filters.CharFilter(method='fullname_filter', lookup_expr='icontains',
                                   widget=TextInput(attrs={'placeholder': 'جستجو ...'}))

    def fullname_filter(self, queryset, name, value):
        queryset = User.objects.filter(is_active=True, is_parent=True).annotate(
            fullname=Concat('first_name', Value(' '), 'last_name'))
        return queryset.filter(Q(fullname__icontains=value))


class TeacherFilter(filters.FilterSet):
    full_name = filters.CharFilter(method='fullname_filter', lookup_expr='icontains',
                                   widget=TextInput(attrs={'placeholder': 'جستجو ...'}))

    def fullname_filter(self, queryset, name, value):
        queryset = User.objects.filter(is_active=True, is_teacher=True).annotate(
            fullname=Concat('first_name', Value(' '), 'last_name'))
        return queryset.filter(Q(fullname__icontains=value))


class ClassFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains',
                              widget=TextInput(attrs={'placeholder': 'جستجو ...'}))

    class Meta:
        model = Classes
        fields = ('grade', 'major', 'name',)


class EMPFormFilter(filters.FilterSet):
    class Meta:
        model = EmploymentForm
        fields = ('status',)


class QuizListFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains',
                              widget=TextInput(attrs={'placeholder': 'جستجو ...'}))

    class Meta:
        model = Quiz
        fields = ('quiz_class', 'name',)

