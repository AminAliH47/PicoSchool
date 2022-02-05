from django import forms

from quiz.models import QuizQuestion, Quiz


class CreateQuestionForm(forms.ModelForm):
    class Meta:
        model = QuizQuestion
        fields = ('text',)


class UpdateQuestionForm(forms.ModelForm):
    class Meta:
        model = QuizQuestion
        fields = ('text', )


class CreateQuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ('name', 'topic', 'quiz_class', 'quiz_book', 'time', 'show_quiz', 'difficulty')
        widgets = {
            'name': forms.TextInput(
                attrs={'placeholder': 'نام آزمون را وارد کنید'}),
            'topic': forms.TextInput(
                attrs={'placeholder': 'موضوع آزمون را وارد کنید'}),
        }


class UpdateQuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ('name', 'topic', 'quiz_class', 'quiz_book', 'active', 'time', 'show_quiz', 'difficulty', 'students')
        widgets = {
            'name': forms.TextInput(
                attrs={'placeholder': 'نام آزمون را وارد کنید'}),
            'topic': forms.TextInput(
                attrs={'placeholder': 'موضوع آزمون را وارد کنید'}),
            'students': forms.CheckboxSelectMultiple,
        }
