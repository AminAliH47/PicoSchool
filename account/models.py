from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Count
from manager.models import Grade, Major
from main.validators import is_valid_national_code

from account.utils.validators import validate_phone_number


class User(AbstractUser):
    SINGLE_OR_MARRIED = (
        ('مجرد', 'مجرد'),
        ('متاهل', 'متاهل'),
    )
    STATUS = (
        ('نیرو آزاد', 'نیرو آزاد'),
        ('شاغل آموزش و پرورش', 'شاغل آموزش و پرورش'),
        ('مامور آموزش و پرورش', 'مامور آموزش و پرورش'),
        ('حق التدریس', 'حق التدریس'),
        ('بازنشسته', 'بازنشسته'),
    )

    # Fields
    is_manager = models.BooleanField(
        default=False,
        verbose_name='مدیر',
    )
    is_parent = models.BooleanField(
        default=False,
        verbose_name='والدین',
    )
    is_teacher = models.BooleanField(
        default=False,
        verbose_name='دبیر',
    )
    is_student = models.BooleanField(
        default=False,
        verbose_name='دانش آموز',
    )
    national_code = models.CharField(
        max_length=10,
        unique=True,
        validators=[is_valid_national_code],
        verbose_name="کد ملی",
    )
    profile_img = models.ImageField(
        upload_to='account/',
        null=True,
        blank=True,
        verbose_name='تصویر پروفایل',
    )
    phone = models.CharField(
        max_length=11,
        null=True,
        blank=True,
        validators=[validate_phone_number],
        verbose_name='شماره تلفن',
    )
    father_name = models.CharField(
        max_length=120,
        null=True,
        blank=True,
        verbose_name="نام پدر",
    )
    address = models.TextField(
        verbose_name="آدرس",
    )
    # -- Student Section
    student_class = models.ForeignKey(
        to="manager.Classes",
        null=True,
        blank=True,
        related_name="student_class",
        on_delete=models.SET_NULL,
        verbose_name="کلاس های دانش آموز",
    )
    grade = models.ForeignKey(
        Grade,
        null=True,
        blank=True,
        related_name="student_grade",
        on_delete=models.SET_NULL,
        verbose_name="مقطع تحصیلی",

    )
    major = models.ForeignKey(
        Major,
        null=True,
        blank=True,
        related_name="student_major",
        on_delete=models.SET_NULL,
        verbose_name="رشته تحصیلی",
    )
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        related_name="student_parent",
        on_delete=models.SET_NULL,
        verbose_name="والدین دانش آموز",
    )
    date_of_birth = models.CharField(
        max_length=200,
        verbose_name="تاریخ تولد",
    )
    # -- Parent Section
    home_phone = models.CharField(
        max_length=11,
        null=True,
        blank=True,
        verbose_name='تلفن منزل',
    )
    job = models.CharField(
        max_length=120,
        null=True,
        blank=True,
        verbose_name="شغل",
    )
    education = models.CharField(
        max_length=120,
        null=True,
        blank=True,
        verbose_name="تحصیلات",
    )
    work_address = models.TextField(
        null=True,
        blank=True,
        verbose_name="آدرس محل کار",
    )
    work_phone = models.CharField(
        max_length=11,
        null=True,
        blank=True,
        verbose_name="تلفن محل کار",
    )
    # -- Teachers Section
    certificate_code = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        verbose_name="کد شناسنامه",
    )
    university = models.CharField(
        max_length=120,
        null=True,
        blank=True,
        verbose_name="دانشگاه محل تحصیل",
    )
    working_hours = models.FloatField(
        null=True,
        blank=True,
        verbose_name="تعداد ساعت های کار",
    )
    basic_salary = models.FloatField(
        null=True,
        blank=True,
        verbose_name="حقوق پایه",
    )
    single_or_married = models.CharField(
        choices=SINGLE_OR_MARRIED,
        max_length=120,
        null=True,
        blank=True,
        verbose_name="مجرد یا متاهل",
    )
    child_num = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="تعداد فرزند",
    )
    spouse_fullname = models.CharField(
        max_length=150,
        null=True,
        blank=True,
        verbose_name="نام و نام خانوادگی همسر",
    )
    spouse_phone = models.CharField(
        max_length=11,
        null=True,
        blank=True,
        verbose_name="تلفن همسر",
    )
    status = models.CharField(
        choices=STATUS,
        max_length=120,
        null=True,
        blank=True,
        verbose_name="وضعیت",
    )

    # Metadata
    class Meta:
        ordering = ('last_name',)

    # Methods
    def __str__(self):
        return self.get_full_name()

    def parent_count(self):
        reviews = User.objects.filter(is_parent=True, is_active=True).aggregate(count=Count('id'))
        count = 0
        if reviews["count"] is not None:
            count = int(reviews["count"])
        return count

    def teacher_count(self):
        reviews = User.objects.filter(is_teacher=True, is_active=True).aggregate(count=Count('id'))
        count = 0
        if reviews["count"] is not None:
            count = int(reviews["count"])
        return count

    def student_count(self):
        reviews = User.objects.filter(is_student=True, is_active=True).aggregate(count=Count('id'))
        count = 0
        if reviews["count"] is not None:
            count = int(reviews["count"])
        return count
