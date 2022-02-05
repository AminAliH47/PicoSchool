from django.shortcuts import render
from main.decorators import allow_user
from manager.models import NoticeBox


@allow_user(["is_superuser", "is_manager", "is_parent"])
def parent_view(request):
    context = {
        "notices": NoticeBox.objects.all().order_by('-publish')[:10],
        "notice_count": NoticeBox.objects.first(),
        "page_title": "پنل والدین",
    }
    return render(request, "parent/parent_panel.html", context)
