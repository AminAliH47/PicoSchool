from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import User

UserAdmin.fieldsets += ('مدیریت', {'fields': ('is_manager',)}),
UserAdmin.fieldsets += ('والدین', {'fields': ('is_parent', 'job', 'education', 'work_address', 'work_phone',)}),
UserAdmin.fieldsets += ('دبیران', {'fields': (
    'is_teacher', 'certificate_code', 'university', 'working_hours', 'basic_salary', 'single_or_married', 'child_num',
    'spouse_fullname', 'spouse_phone', 'status',)}),
UserAdmin.fieldsets += ('دانش آموزان',
                        {'fields': (
                            'is_student', 'father_name', 'grade', 'major', 'student_class', 'parent',
                            'home_phone', 'address', 'date_of_birth')}),
UserAdmin.fieldsets[2][1]['fields'] = ('is_active',
                                       'is_superuser',
                                       'is_staff',
                                       'phone',
                                       'national_code',
                                       'profile_img',
                                       'groups',
                                       'user_permissions',
                                       )
UserAdmin.list_display = (
    'first_name', 'last_name', 'national_code', 'is_manager', 'is_parent', 'is_teacher', 'is_student'
)
UserAdmin.list_filter += ('is_manager', 'is_parent', 'is_teacher', 'is_student',)

admin.site.register(User, UserAdmin)
