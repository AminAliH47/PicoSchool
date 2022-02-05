import django_filters as filters
from django.db.models import Value, Q
from django.db.models.functions import Concat
from django.forms import TextInput

from account.models import User
from .models import QuizResult


class QuizResultFilter(filters.FilterSet):
    full_name = filters.CharFilter(method='fullname_filter', lookup_expr='icontains',
                                   widget=TextInput(attrs={'placeholder': 'جستجو ...'}))

    def fullname_filter(self, value):
        queryset = User.objects.filter(is_active=True, is_student=True).annotate(
            fullname=Concat('first_name', Value(' '), 'last_name'))
        print(value)
        return queryset.filter(Q(fullname__icontains=value))

    class Meta:
        model = QuizResult
        fields = ('user', 'full_name')
