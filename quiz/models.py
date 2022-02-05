from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils import timezone
from django.utils.html import format_html
from account.models import User
from extensions.utils import jalili_converter
from manager.models import Classes, Books
import uuid


class Quiz(models.Model):
    """
    Model for Main Quiz
    """
    DIFF_CHOICES = (
        ('ساده', 'ساده'),
        ('متوسط', 'متوسط'),
        ('سخت', 'سخت'),
    )

    # Fields
    uuid = models.UUIDField(
        max_length=120,
        default=uuid.uuid4,
        verbose_name='آیدی یونیک'
    )
    name = models.CharField(
        max_length=120,
        verbose_name='نام آزمون'
    )
    topic = models.CharField(
        max_length=120,
        null=True,
        blank=True,
        verbose_name='موضوع آزمون'
    )
    quiz_class = models.ForeignKey(
        Classes,
        on_delete=models.CASCADE,
        related_name='quiz_classes',
        verbose_name='کلاس آزمون'
    )
    quiz_book = models.ForeignKey(
        Books,
        on_delete=models.CASCADE,
        related_name='quiz_book',
        verbose_name='درس آزمون'
    )
    number_of_question = models.IntegerField(
        null=True,
        blank=True,
        verbose_name='تعداد سوالات'
    )
    time = models.IntegerField(
        help_text="بر اساس (دقیقه)",
        verbose_name='زمان آزمون'
    )
    show_quiz = models.BooleanField(
        default=False,
        verbose_name='نمایش سوال ها در صفحات جدا'
    )
    required_score_to_pass = models.IntegerField(
        null=True,
        blank=True,
        help_text='نمره برای قبولی بر اساس (درصد)',
        verbose_name='نمره برای قبولی'
    )
    difficulty = models.CharField(
        choices=DIFF_CHOICES,
        max_length=10,
        verbose_name='سختی آزمون'
    )
    active = models.BooleanField(
        default=False,
        verbose_name='فعال / غیرفعال'
    )
    students = models.ManyToManyField(
        User,
        related_name='quiz_student',
        blank=True,
        verbose_name='کاربران',
        limit_choices_to={'is_student': True}
    )
    created = models.DateTimeField(
        default=timezone.now,
        verbose_name='زمان ساخت'
    )
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name="آخرین بروزرسانی",
    )

    # Metadata
    class Meta:
        verbose_name = "آزمون"
        verbose_name_plural = '01. آزمون ها'
        ordering = ('-created',)

    # Methods
    def __str__(self):
        return self.name

    def questions(self):
        return self.question_quiz.all()

    def jdate(self):
        return jalili_converter(self.created)


class QuizQuestion(models.Model):
    """
    Model for main quiz questions
    """
    QUS_TYPE = (
        ('چهار گزینه ای', 'چهار گزینه ای'),
        ('تشریحی', 'تشریحی'),
    )

    # Fields
    id = models.BigIntegerField(
        unique=True,
        primary_key=True,
    )
    text = RichTextUploadingField(
        max_length=120,
        verbose_name='عنوان سوال',
    )
    quiz = models.ForeignKey(
        Quiz,
        on_delete=models.CASCADE,
        related_name='question_quiz',
        verbose_name='آزمون سوال',
    )
    question_type = models.CharField(
        choices=QUS_TYPE,
        max_length=20,
        default='چهار گزینه ای',
        verbose_name='نوع سوال'
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='زمان ساخت'
    )

    # Metadata
    class Meta:
        verbose_name = "سوال"
        verbose_name_plural = '02. سوال های آزمون'

    # Methods
    def __str__(self):
        return format_html(self.text)

    def get_answers(self):
        return self.answer_question.all()


class QuizMultipleAnswers(models.Model):
    """
    Model for Answer multiple choice questions
    """

    # Fields
    text = models.CharField(
        max_length=120,
        verbose_name='عنوان پاسخ',
    )
    correct = models.BooleanField(
        default=False,
        verbose_name='پاسخ درست',
    )
    question = models.ForeignKey(
        QuizQuestion,
        on_delete=models.CASCADE,
        related_name='answer_multi_question',
        verbose_name='سوال پاسخ',
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='زمان ساخت',
    )

    # Metadata
    class Meta:
        verbose_name = "پاسخ"
        verbose_name_plural = '03. پاسخ های آزمون چهار گزینه ای'

    # Methods
    def __str__(self):
        return self.text


class QuizDescAnswers(models.Model):
    """
    Model for Answer description questions
    """

    # Fields
    text = models.TextField(
        verbose_name='متن',
    )
    question = models.ForeignKey(
        QuizQuestion,
        on_delete=models.CASCADE,
        related_name='answer_desc_question',
        verbose_name='سوال پاسخ',
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='زمان ساخت'
    )

    # Metadata
    class Meta:
        verbose_name = "پاسخ"
        verbose_name_plural = '04. پاسخ های آزمون تشریحی'

    # Methods
    def __str__(self):
        return self.question


class QuizResult(models.Model):
    """
    Model for Main quiz result
    """

    # Fields
    quiz = models.ForeignKey(
        Quiz,
        on_delete=models.CASCADE,
        related_name='result_quiz',
        verbose_name='نتیجه آزمون',
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='result_user',
        verbose_name='نتیجه برای کاربر',
    )
    data = models.JSONField(
        verbose_name='اطلاعات'
    )

    # Metadata
    class Meta:
        verbose_name = "نتیجه"
        verbose_name_plural = '4. نتایج آزمون'

    # Methods
    def __str__(self):
        return str(self.pk)
