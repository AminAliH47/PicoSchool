from django.contrib import admin
from django.urls import (
    path,
    include,
)
from django.conf.urls.static import static
from PicoSchool import settings

admin.site.site_header = "مدیریت PicoSchool"

urlpatterns = [
    path('', include('account.urls')),
    path('', include('main.urls')),
    path('manager/', include('manager.urls')),
    path('parent/', include('parent.urls')),
    path('teacher/', include('teacher.urls')),
    path('student/', include('student.urls')),
    path('poll/', include('poll.urls')),
    path('quiz/', include('quiz.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('pwa.urls')),
    path('pico-school/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
