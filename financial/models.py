from django.db import models


class Financial(models.Model):
    card_number = models.CharField(max_length=19, verbose_name="شماره کارت")

