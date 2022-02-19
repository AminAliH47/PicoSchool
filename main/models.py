from django.db import models


class SiteSetting(models.Model):
    COLOR_THEME = (
        ("green", "سبز"),
        ("orange", "نارنجی"),
        ("yellow", "زرد"),
    )
    MENU_THEME = (
        ('waterfall', 'منو آبشاری'),
        ("four_rooms", "منو چارخونه ای"),
    )

    # Fields
    school_name = models.CharField(
        max_length=20,
        verbose_name="نام مدرسه",
    )
    school_logo = models.ImageField(
        upload_to="main/school_logo/",
        verbose_name="لوگو مدرسه",
    )
    site_color = models.CharField(
        max_length=10,
        choices=COLOR_THEME,
        default="green",
        verbose_name="رنگ سایت",
    )
    site_menu_theme = models.CharField(
        max_length=15,
        choices=MENU_THEME,
        default="waterfall",
        verbose_name="تم منو سایت",
    )
    favicon = models.ImageField(
        upload_to="main/school_logo/",
        verbose_name="فاآیکون",
        null=True,
        blank=True,
    )

    # Metadata
    class Meta:
        verbose_name = 'تنظیمات سایت'
        verbose_name_plural = '01. تنظیمات سایت'

    # Methods
    def __str__(self):
        return self.school_name
