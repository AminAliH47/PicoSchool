from django import forms
from django.contrib.admin.views import autocomplete
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib.auth.hashers import make_password

from .models import User

widget_fields = {
    'first_name': forms.TextInput(
        attrs={'placeholder': 'نام را وارد کنید'}),
    'last_name': forms.TextInput(
        attrs={'placeholder': 'نام خانوادگی را وارد کنید'}),
    'national_code': forms.TextInput(
        attrs={'placeholder': 'کد ملی را وارد کنید'}),
    'phone': forms.TextInput(
        attrs={'placeholder': 'شماره تلفن را وارد کنید'}),
    'home_phone': forms.TextInput(
        attrs={'placeholder': 'شماره منزل را وارد کنید'}),
    'date_of_birth': forms.TextInput(
        attrs={'placeholder': 'تاریخ تولد را وارد کنید'}),
    'father_name': forms.TextInput(
        attrs={'placeholder': 'نام پدر را وارد کنید'}),
    'address': forms.Textarea(
        attrs={'placeholder': 'آدرس را وارد کنید'}),
    'password': forms.PasswordInput(),
}


class CreateStudentUserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CreateStudentUserForm, self).__init__(*args, **kwargs)
        self.fields['parent'].queryset = User.objects.filter(is_active=True, is_parent=True)
        self.fields['parent'].required = True
        self.fields['grade'].required = True
        self.fields['date_of_birth'].required = True
        self.fields['father_name'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['home_phone'].required = True
        self.fields['student_class'].required = True

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'national_code', 'phone', 'home_phone', 'date_of_birth', 'father_name',
            'address', 'password', 'profile_img', 'student_class', 'parent', 'grade', 'major', 'is_student',
            'is_parent', 'is_teacher'
        )
        widget_fields['parent'] = forms.Select(attrs={"class": "selectInput"})
        widgets = widget_fields

        def save(self, commit=True):
            user = super().save(commit=False)
            user.set_password(self.cleaned_data['password'])
            if commit:
                user.save()
            return user


class UpdateStudentUserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UpdateStudentUserForm, self).__init__(*args, **kwargs)
        self.fields['parent'].queryset = User.objects.filter(is_active=True, is_parent=True)
        self.fields['parent'].required = True
        self.fields['grade'].required = True
        self.fields['date_of_birth'].required = True
        self.fields['father_name'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['home_phone'].required = True
        self.fields['student_class'].required = True

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'national_code', 'phone', 'home_phone', 'date_of_birth', 'father_name',
            'address', 'profile_img', 'student_class', 'parent', 'grade', 'major', 'is_student'
        )
        widget_fields['parent'] = forms.Select(attrs={"class": "selectInput"})
        widgets = widget_fields


class CreateParentUserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CreateParentUserForm, self).__init__(*args, **kwargs)
        self.fields['date_of_birth'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['home_phone'].required = True
        self.fields['phone'].required = True
        self.fields['job'].required = True
        self.fields['education'].required = True
        self.fields['work_address'].required = False
        self.fields['work_phone'].required = False

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'national_code', 'phone', 'home_phone', 'date_of_birth', 'father_name',
            'address', 'password', 'profile_img', 'job', 'education', 'work_address', 'work_phone', 'is_parent'
        )
        widget_fields['work_phone'] = forms.TextInput(attrs={'placeholder': 'شماره محل کار را وارد کنید'})
        widget_fields['work_address'] = forms.Textarea(attrs={'placeholder': 'آدرس محل کار را وارد کنید'})
        widget_fields['job'] = forms.TextInput(attrs={'placeholder': 'شغل را وارد کنید'})
        widget_fields['education'] = forms.TextInput(attrs={'placeholder': 'تحصیلات را وارد کنید'})
        widgets = widget_fields

        def save(self, commit=True):
            user = super().save(commit=False)
            user.set_password(self.cleaned_data['password'])
            if commit:
                user.save()
            return user


class UpdateParentUserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UpdateParentUserForm, self).__init__(*args, **kwargs)
        self.fields['date_of_birth'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['home_phone'].required = True
        self.fields['phone'].required = True
        self.fields['job'].required = True
        self.fields['education'].required = True
        self.fields['work_address'].required = False
        self.fields['work_phone'].required = False

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'national_code', 'phone', 'home_phone', 'date_of_birth', 'father_name',
            'address', 'profile_img', 'job', 'education', 'work_address', 'work_phone', 'is_parent'
        )
        widget_fields['work_phone'] = forms.TextInput(attrs={'placeholder': 'شماره محل کار را وارد کنید'})
        widget_fields['work_address'] = forms.Textarea(attrs={'placeholder': 'آدرس محل کار را وارد کنید'})
        widget_fields['job'] = forms.TextInput(attrs={'placeholder': 'شغل را وارد کنید'})
        widget_fields['education'] = forms.TextInput(attrs={'placeholder': 'تحصیلات را وارد کنید'})
        widgets = widget_fields


class CreateTeacherUserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CreateTeacherUserForm, self).__init__(*args, **kwargs)
        self.fields['date_of_birth'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['home_phone'].required = True
        self.fields['phone'].required = True
        self.fields['education'].required = True
        self.fields['certificate_code'].required = True
        self.fields['university'].required = True
        self.fields['working_hours'].required = True
        self.fields['basic_salary'].required = True
        self.fields['single_or_married'].required = True
        self.fields['status'].required = True

    def clean_spouse_fullname(self):
        data = self.cleaned_data['spouse_fullname']
        single_or_married = self.cleaned_data.get('single_or_married')
        if single_or_married == "متاهل":
            spouse_fullname = self.cleaned_data['spouse_fullname']
            if spouse_fullname is None:
                raise forms.ValidationError("این فیلد مورد نیاز است")
        return data

    def clean_spouse_phone(self):
        data = self.cleaned_data['spouse_phone']
        single_or_married = self.cleaned_data.get('single_or_married')
        if single_or_married == "متاهل":
            spouse_phone = self.cleaned_data['spouse_phone']
            if spouse_phone is None:
                raise forms.ValidationError("این فیلد مورد نیاز است")
        return data

    def clean_child_num(self):
        data = self.cleaned_data['child_num']
        single_or_married = self.cleaned_data.get('single_or_married')
        if single_or_married == "متاهل":
            child_num = self.cleaned_data['child_num']
            if child_num is None:
                raise forms.ValidationError("این فیلد مورد نیاز است")
        return data

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'national_code', 'phone', 'home_phone', 'date_of_birth', 'father_name',
            'address', 'password', 'profile_img', 'education', 'certificate_code', 'university',
            'working_hours', 'basic_salary', 'single_or_married', 'child_num', 'spouse_fullname', 'spouse_phone',
            'status', 'is_teacher',
        )
        widget_fields['education'] = forms.TextInput(attrs={'placeholder': 'تحصیلات را وارد کنید'})
        widget_fields['certificate_code'] = forms.TextInput(attrs={'placeholder': 'شماره شناسنامه'})
        widget_fields['university'] = forms.TextInput(attrs={'placeholder': 'دانشگاه محل تحصیل'})
        widget_fields['working_hours'] = forms.NumberInput(attrs={'placeholder': 'تعداد ساعت های کار'})
        widget_fields['basic_salary'] = forms.NumberInput(attrs={'placeholder': 'حقوق پایه'})
        widget_fields['child_num'] = forms.NumberInput(attrs={'placeholder': 'تعداد فرزند'})
        widget_fields['spouse_fullname'] = forms.TextInput(attrs={'placeholder': 'نام و نام خانوادگی همسر'})
        widget_fields['spouse_phone'] = forms.TextInput(attrs={'placeholder': 'تلفن همسر'})
        widgets = widget_fields

        def save(self, commit=True):
            user = super().save(commit=False)
            user.set_password(self.cleaned_data['password'])
            if commit:
                user.save()
            return user


class UpdateTeacherUserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UpdateTeacherUserForm, self).__init__(*args, **kwargs)
        self.fields['date_of_birth'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['home_phone'].required = True
        self.fields['phone'].required = True
        self.fields['education'].required = True
        self.fields['certificate_code'].required = True
        self.fields['university'].required = True
        self.fields['working_hours'].required = True
        self.fields['basic_salary'].required = True
        self.fields['single_or_married'].required = True
        self.fields['status'].required = True

    def clean_spouse_fullname(self):
        data = self.cleaned_data['spouse_fullname']
        single_or_married = self.cleaned_data.get('single_or_married')
        if single_or_married == "متاهل":
            spouse_fullname = self.cleaned_data['spouse_fullname']
            if spouse_fullname is None:
                raise forms.ValidationError("این فیلد مورد نیاز است")
        return data

    def clean_spouse_phone(self):
        data = self.cleaned_data['spouse_phone']
        single_or_married = self.cleaned_data.get('single_or_married')
        if single_or_married == "متاهل":
            spouse_phone = self.cleaned_data['spouse_phone']
            if spouse_phone is None:
                raise forms.ValidationError("این فیلد مورد نیاز است")
        return data

    def clean_child_num(self):
        data = self.cleaned_data['child_num']
        single_or_married = self.cleaned_data.get('single_or_married')
        if single_or_married == "متاهل":
            child_num = self.cleaned_data['child_num']
            if child_num is None:
                raise forms.ValidationError("این فیلد مورد نیاز است")
        return data

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'national_code', 'phone', 'home_phone', 'date_of_birth', 'father_name',
            'address', 'profile_img', 'education', 'certificate_code', 'university',
            'working_hours', 'basic_salary', 'single_or_married', 'child_num', 'spouse_fullname', 'spouse_phone',
            'status', 'is_teacher',
        )
        widget_fields['education'] = forms.TextInput(attrs={'placeholder': 'تحصیلات را وارد کنید'})
        widget_fields['certificate_code'] = forms.TextInput(attrs={'placeholder': 'شماره شناسنامه'})
        widget_fields['university'] = forms.TextInput(attrs={'placeholder': 'دانشگاه محل تحصیل'})
        widget_fields['working_hours'] = forms.NumberInput(attrs={'placeholder': 'تعداد ساعت های کار'})
        widget_fields['basic_salary'] = forms.NumberInput(attrs={'placeholder': 'حقوق پایه'})
        widget_fields['child_num'] = forms.NumberInput(attrs={'placeholder': 'تعداد فرزند'})
        widget_fields['spouse_fullname'] = forms.TextInput(attrs={'placeholder': 'نام و نام خانوادگی همسر'})
        widget_fields['spouse_phone'] = forms.TextInput(attrs={'placeholder': 'تلفن همسر'})
        widgets = widget_fields
