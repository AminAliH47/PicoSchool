# Generated by Django 3.2 on 2022-02-19 05:36

import account.utils.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='certificate_code',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='کد شناسنامه'),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_of_birth',
            field=models.CharField(max_length=10, verbose_name='تاریخ تولد'),
        ),
        migrations.AlterField(
            model_name='user',
            name='education',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='تحصیلات'),
        ),
        migrations.AlterField(
            model_name='user',
            name='father_name',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='نام پدر'),
        ),
        migrations.AlterField(
            model_name='user',
            name='job',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='شغل'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=11, null=True, validators=[account.utils.validators.validate_phone_number], verbose_name='شماره تلفن'),
        ),
        migrations.AlterField(
            model_name='user',
            name='single_or_married',
            field=models.CharField(blank=True, choices=[('مجرد', 'مجرد'), ('متاهل', 'متاهل')], max_length=5, null=True, verbose_name='مجرد یا متاهل'),
        ),
        migrations.AlterField(
            model_name='user',
            name='spouse_fullname',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='نام و نام خانوادگی همسر'),
        ),
        migrations.AlterField(
            model_name='user',
            name='status',
            field=models.CharField(blank=True, choices=[('نیرو آزاد', 'نیرو آزاد'), ('شاغل آموزش و پرورش', 'شاغل آموزش و پرورش'), ('مامور آموزش و پرورش', 'مامور آموزش و پرورش'), ('حق التدریس', 'حق التدریس'), ('بازنشسته', 'بازنشسته')], max_length=20, null=True, verbose_name='وضعیت'),
        ),
        migrations.AlterField(
            model_name='user',
            name='university',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='دانشگاه محل تحصیل'),
        ),
    ]
