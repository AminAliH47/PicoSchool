import django_filters as filters
from django import forms
from django.db.models import (
    Value,
    Q,
)
from django.db.models.functions import Concat
from account.models import User
from quiz.models import (
    QuizResult,
    Quiz,
)


class QuizResultFilter(filters.FilterSet):
    """
    Filter the Main quiz result
    """
    full_name = filters.CharFilter(method='fullname_filter', lookup_expr='icontains',
                                   widget=forms.TextInput(attrs={'placeholder': 'جستجو ...'}))
    quiz = filters.ModelChoiceFilter(
        queryset=Quiz.objects.all(),
        widget=forms.Select(attrs={
            "onchange": "this.form.submit()",
        }),
    )
    def fullname_filter(self, value):
        queryset = User.objects.filter(is_active=True, is_student=True).annotate(
            fullname=Concat('first_name', Value(' '), 'last_name'))
        return queryset.filter(Q(fullname__icontains=value))

    class Meta:
        model = QuizResult
        fields = ('full_name', 'quiz',)
