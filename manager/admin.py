from django.contrib import admin
from manager.models import (
    EventCalendar,
    ExternalEventCalendar,
    NoticeBox,
    Classes,
    Grade,
    Major,
    Books,
    Attendance,
    Assign,
    HomeWork,
    EmploymentForm,
)


class EventCalendarAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'publish')


admin.site.register(EventCalendar, EventCalendarAdmin)


class ExternalEventCalendarAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'publish')


admin.site.register(ExternalEventCalendar, ExternalEventCalendarAdmin)

admin.site.register(NoticeBox)


class BooksAdmin(admin.ModelAdmin):
    search_fields = ('books_class',)


admin.site.register(Books, BooksAdmin)


class ClassesAdmin(admin.ModelAdmin):
    search_fields = ('name', 'teacher', 'books',)
    autocomplete_fields = ('teacher', 'books',)


admin.site.register(Classes, ClassesAdmin)


class GradeAdmin(admin.ModelAdmin):
    search_fields = ('name',)


admin.site.register(Grade, GradeAdmin)


class MajorAdmin(admin.ModelAdmin):
    search_fields = ('name',)


admin.site.register(Major, MajorAdmin)


class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'jdate', 'book',)


admin.site.register(Attendance, AttendanceAdmin)
admin.site.register(Assign)
admin.site.register(HomeWork)


class EmploymentFormAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'status',)
    list_filter = ('status',)


admin.site.register(EmploymentForm, EmploymentFormAdmin)
