from datetime import datetime
import jdatetime
from django.db import models
from django.db.models import Count
from django.urls import reverse_lazy
from django.utils import timezone

from extensions.utils import jalili_converter, change_month


# Events (Calendar) Section
class EventCalendar(models.Model):
    """
    Model for Main calendar events
    """

    # Fields
    id = models.CharField(
        max_length=100,
        unique=True,
        primary_key=True,
        verbose_name="آیدی رویدار",
    )
    title = models.CharField(
        max_length=120,
        verbose_name="عنوان رویداد",
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name='توضیحات رویداد',
    )
    start = models.CharField(
        max_length=60,
        verbose_name="شروع رویداد",
    )
    end = models.CharField(
        max_length=60,
        default=start,
        verbose_name="پایان رویداد",
    )
    backgroundColor = models.CharField(
        max_length=20,
        verbose_name="رنگ زمینه رویداد",
    )
    borderColor = models.CharField(
        max_length=20,
        verbose_name="رنگ خط رویداد",
    )
    publish = models.DateTimeField(
        auto_now_add=True,
        verbose_name="زمان ساخت",
    )

    # Metadata
    class Meta:
        verbose_name = 'رویداد'
        verbose_name_plural = '01. تقویم رویداد ها'

    # Methods
    def __str__(self):
        return self.title

    def jstart(self):
        start = self.start[:10]
        date_time_obj = datetime.strptime(start, '%Y-%m-%d')
        return change_month(jdatetime.date.fromgregorian(date=datetime.date(date_time_obj)))

    def count(self):
        reviews = EventCalendar.objects.all().aggregate(count=Count('id'))
        count = 0
        if reviews["count"] is not None:
            count = int(reviews["count"])
        return count


class ExternalEventCalendar(models.Model):
    """
    Model for external Main calendar events
    """

    # Fields
    id = models.CharField(
        max_length=100,
        unique=True,
        primary_key=True,
        verbose_name="آیدی رویدار",
    )
    title = models.CharField(
        max_length=120,
        verbose_name="عنوان رویداد",
    )
    backgroundColor = models.CharField(
        max_length=20,
        verbose_name="رنگ زمینه رویداد",
    )
    borderColor = models.CharField(
        max_length=20,
        verbose_name="رنگ خط رویداد",
    )
    publish = models.DateTimeField(
        auto_now_add=True,
        verbose_name="زمان ساخت",
    )

    # Metadata
    class Meta:
        verbose_name = 'رویداد'
        verbose_name_plural = '1_02. رویداد های اضافه نشده'

    # Methods
    def __str__(self):
        return self.title


# Notice Box Section
class NoticeBox(models.Model):
    """
    Model for main Notice box
    """

    # Fields
    writer = models.ForeignKey(
        to='account.User',
        on_delete=models.CASCADE,
        verbose_name="نویسنده اعلان",
    )
    title = models.CharField(
        max_length=120,
        verbose_name="عنوان اعلان",
    )
    description = models.TextField(
        max_length=350,
        verbose_name="متن اعلان",
    )
    publish = models.DateTimeField(
        auto_now_add=True,
        verbose_name="زمان ساخت",
    )

    # Metadata
    class Meta:
        verbose_name = 'اعلان'
        verbose_name_plural = '02. تابلو اعلانات'

    # Methods
    def __str__(self):
        return self.title

    def jpublish(self):
        return jalili_converter(self.publish)

    def count(self):
        reviews = NoticeBox.objects.all().aggregate(count=Count('id'))
        count = 0
        if reviews["count"] is not None:
            count = int(reviews["count"])
        return count


# Grade Section
class Grade(models.Model):
    """
    Model for School grads
    """

    # Fields
    name = models.CharField(
        max_length=120,
        verbose_name="نام مقطع",
    )

    # Metadata
    class Meta:
        verbose_name = 'مقطع'
        verbose_name_plural = '03. مقاطع تحصیلی'

    # Methods
    def __str__(self):
        return self.name


# Major Section
class Major(models.Model):
    """
    Model for School major
    """

    # Fields
    name = models.CharField(
        max_length=120,
        verbose_name="نام رشته تحصیلی",
    )

    # Metadata
    class Meta:
        verbose_name = 'رشته'
        verbose_name_plural = '04. رشته های تحصیلی'

    # Methods
    def __str__(self):
        return self.name


# Classes Section
class Classes(models.Model):
    """
    Model for school classes
    """

    # Fields
    name = models.CharField(
        max_length=120,
        verbose_name="نام کلاس",
    )
    code = models.CharField(
        max_length=10,
        null=True,
        blank=True,
        verbose_name="شماره کلاس",
    )
    books = models.ManyToManyField(
        to="manager.Books",
        related_name="books_class",
        verbose_name="کتاب های کلاس",
    )
    teacher = models.ManyToManyField(
        to='account.User',
        related_name="teacher_class",
        limit_choices_to={"is_teacher": True},
        verbose_name="معلم کلاس",
    )
    grade = models.ForeignKey(
        Grade,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="grade_classes",
        verbose_name="مقطع",
    )
    major = models.ForeignKey(
        Major,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="major_classes",
        verbose_name="رشته",
    )

    # Metadata
    class Meta:
        verbose_name = 'کلاس'
        verbose_name_plural = '05. کلاس ها'

    # Methods
    def __str__(self):
        return self.name

    def student_count(self):
        print(Classes.objects.filter(student_class="1"))
        reviews = Classes.objects.filter(student_class__id=self.id).aggregate(count=Count('student_class'))
        count = 0
        if reviews["count"] is not None:
            count = int(reviews["count"])
        return count


class Books(models.Model):
    """
    Model for class books
    """

    # Fields
    name = models.CharField(
        max_length=150,
        verbose_name="نام کتاب درسی",
    )
    units = models.IntegerField(
        verbose_name="تعداد واحد",
    )
    teacher = models.ManyToManyField(
        to='account.User',
        related_name="teacher_book",
        limit_choices_to={"is_teacher": True},
        blank=True,
        verbose_name="دبیر کتاب",
    )
    grade = models.ForeignKey(
        Grade,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="grade_books",
        verbose_name="مقطع",
    )
    major = models.ManyToManyField(
        Major,
        blank=True,
        related_name="major_books",
        verbose_name="رشته",
    )

    # Metadata
    class Meta:
        verbose_name = 'کتاب'
        verbose_name_plural = '06. کتاب ها'

    # Methods
    def __str__(self):
        return self.name


jalali_date = str(jdatetime.date.fromgregorian(date=timezone.now()))


class Attendance(models.Model):
    """
    Model for students attendance
    this model will create a list of student for a book on a special date
    """

    # Fields
    attendance_class = models.ForeignKey(
        Classes,
        on_delete=models.CASCADE,
        related_name="attendance_class",
        verbose_name="کلاس",
    )
    book = models.ForeignKey(
        Books,
        on_delete=models.CASCADE,
        related_name="attendance_book",
        verbose_name="کتاب",
    )
    date = models.CharField(
        max_length=120,
        default=jalali_date,
        verbose_name="تاریخ کلاس",
    )
    create = models.DateTimeField(
        default=timezone.now,
        verbose_name="تاریخ ساخت کلاس",
    )
    teacher = models.ForeignKey(
        to='account.User',
        on_delete=models.CASCADE,
        related_name="attendance_teacher",
        default=1,
        verbose_name="دبیر",
    )

    # Metadata
    class Meta:
        verbose_name = 'حضور و غیاب'
        verbose_name_plural = '07. حضور و غیاب ها'
        ordering = ('-create',)

    # Methods
    def __str__(self):
        return f"{self.attendance_class.name} - {self.jdate()}"

    def jdate(self):
        return change_month(self.date)

    jdate.short_description = 'تاریخ کلاس'

    def get_absolute_url(self):
        return reverse_lazy('main:attendance_detail', kwargs={'pk': self.pk, 'date': self.date})


class Assign(models.Model):
    """
    this model is for Establishing a relationship between Attendance and Students Status
    """
    ATTENDANCE_STATUS = (
        ('حاضر', 'حاضر'),
        ('حاضر (با تاخیر)', 'حاضر (با تاخیر)'),
        ('غایب', 'غایب'),
    )

    # Fields
    attendance = models.ForeignKey(
        Attendance,
        on_delete=models.CASCADE,
        related_name="att_assign",
    )
    student = models.ForeignKey(
        to='account.User',
        unique=False,
        on_delete=models.CASCADE,
        related_name='stu_assign',
    )
    attendance_status = models.CharField(
        choices=ATTENDANCE_STATUS,
        max_length=120,
        null=True,
        blank=True,
        verbose_name="وضعیت حضور و غیاب",
    )
    attendance_note = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name='توضیحات بیشتر',
    )

    # Metadata
    class Meta:
        verbose_name = "ارتباط"
        verbose_name_plural = 'ارتباط ها'

    # Methods
    def __str__(self):
        return f"{self.attendance} - {self.student} - {self.attendance_status}"


# Report card Section
class ReportCard(models.Model):
    """
    Model for Report card (incomplete)
    """

    # Fields
    student = models.ForeignKey(
        to='account.User',
        on_delete=models.CASCADE,
        related_name='stu_rc',
        verbose_name='دانش آموز',
    )
    report_card = models.TextField(
        verbose_name='کارنامه',
    )

    # Methods
    def __str__(self):
        return self.student


# Home work status
class HomeWork(models.Model):
    """
    Model for students home work
    """

    # Fields
    attendance = models.ForeignKey(
        Attendance,
        on_delete=models.CASCADE,
        related_name='att_home_work',
        verbose_name='برای کلاس',
    )
    title = models.CharField(
        max_length=120,
        verbose_name='عنوان',
    )
    description = models.TextField(
        verbose_name='شرح تکلیف',
        blank=True,
    )
    create = models.DateTimeField(
        default=timezone.now,
        verbose_name="تاریخ ساخت تکلیف",
    )

    # Metadata
    class Meta:
        verbose_name = "تکلیف"
        verbose_name_plural = '08. تکالیف'
        ordering = ('-create',)

    # Methods
    def __str__(self):
        return self.title

    @property
    def date(self):
        return change_month(self.attendance.date)


FORM_STATUS = (
    ('بررسی شده', 'بررسی شده'),
    ('در انتظار بررسی', 'در انتظار بررسی'),
    ('رد شده', 'رد شده'),
)


class EmploymentForm(models.Model):
    """
    Model for student employment form request
    """

    # Fields
    student = models.ForeignKey(
        to='account.User',
        on_delete=models.CASCADE,
        related_name='stu_emp_form',
        verbose_name='دانش آموز',
    )
    organ = models.CharField(
        max_length=120,
        verbose_name='ارگان مورد نظر',
    )
    status = models.CharField(
        max_length=120,
        choices=FORM_STATUS,
        default='در انتظار بررسی',
        verbose_name='وضعیت',
    )
    form_image = models.ImageField(
        upload_to='main/employment-form/',
        null=True,
        blank=True,
        verbose_name='تصویر فرم',
    )
    create = models.DateTimeField(
        default=timezone.now,
        verbose_name="تاریخ ساخت فرم",
    )

    # Metadata
    class Meta:
        verbose_name = "فرم"
        verbose_name_plural = '09. فرم های اشتغال به تحصیل'
        ordering = ('-create',)

    # Methods
    def __str__(self):
        return self.student.get_full_name()

    def all_count(self):
        reviews = EmploymentForm.objects.all().aggregate(count=Count('id'))
        count = 0
        if reviews["count"] is not None:
            count = int(reviews["count"])
        return count
