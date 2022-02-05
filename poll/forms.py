from django import forms

from .models import Poll, PollOptions


class CreatePollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ('question', 'active', 'for_user',)
        widgets = {
            'question': forms.TextInput(
                attrs={'placeholder': 'عنوان نظرسنجی را وارد کنید'}),
        }

