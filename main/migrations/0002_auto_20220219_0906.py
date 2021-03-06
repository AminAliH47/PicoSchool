# Generated by Django 3.2 on 2022-02-19 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitesetting',
            name='school_name',
            field=models.CharField(max_length=20, verbose_name='نام مدرسه'),
        ),
        migrations.AlterField(
            model_name='sitesetting',
            name='site_menu_theme',
            field=models.CharField(choices=[('waterfall', 'منو آبشاری'), ('four_rooms', 'منو چارخونه ای')], default='waterfall', max_length=15, verbose_name='تم منو سایت'),
        ),
    ]
