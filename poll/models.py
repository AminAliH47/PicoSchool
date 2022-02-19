from django.db import models
from django.db.models import Count
from django.utils import timezone
from account.models import User


class Poll(models.Model):
    """
    Model for Main Poll
    """

    # Fields
    USER = (
        ('all', 'همه'),
        ('teacher', 'دبیران'),
        ('parent', 'والدین'),
        ('student', 'دانش آموزان'),
    )
    question = models.CharField(
        max_length=30,
        verbose_name='عنوان سوال',
    )
    active = models.BooleanField(
        default=False,
        verbose_name='فعال / غیرفعال',
    )
    for_user = models.CharField(
        max_length=15,
        choices=USER,
        default='all',
        verbose_name='برای کاربران',
    )
    users = models.ManyToManyField(
        User,
        related_name='poll_user',
        blank=True,
        verbose_name='کاربران',
    )
    create = models.DateTimeField(
        default=timezone.now,
        verbose_name='زمان ساخت',
    )

    # Metadata
    class Meta:
        verbose_name = 'نظرسنجی'
        verbose_name_plural = '1. نظرسنجی ها'
        ordering = ('-create',)

    # Methods
    def __str__(self):
        return self.question

    @property
    def all_count(self):
        polls = Poll.objects.all().count()
        return polls


class PollOptions(models.Model):
    """
    Model for Main poll options
    """

    # Fields
    poll = models.ForeignKey(
        Poll,
        on_delete=models.CASCADE,
        related_name='poll_option',
        verbose_name='برای نظرسنجی',
    )
    option = models.CharField(
        max_length=30,
        verbose_name='گزینه',
    )
    option_count = models.IntegerField(
        default=0,
        verbose_name='شمارش گزینه',
    )

    # Metadata
    class Meta:
        verbose_name = 'گزینه'
        verbose_name_plural = '2. گزینه ها'

    # Methods
    def __str__(self):
        return self.option
