from account.models import User
from main.models import SiteSetting
from manager.models import (
    EventCalendar,
    ExternalEventCalendar,
    NoticeBox,
    EmploymentForm,
)
from poll.models import Poll


def user_context_processor(request):
    users = User.objects.filter(is_active=True)
    employment_form = EmploymentForm.objects.first()
    poll = Poll.objects.first()
    return {
        'employment_form': employment_form,
        'poll': poll,
        'users': users,
    }


def calendar_context_processor(request):
    event = EventCalendar.objects.all()
    dropdown_events = EventCalendar.objects.all().order_by('-publish')[:3]
    ex_event = ExternalEventCalendar.objects.all().order_by('-publish')
    event_count = EventCalendar.objects.first()
    return {
        'events': event,
        'dropdown_events': dropdown_events,
        'ex_events': ex_event,
        'event_count': event_count,
    }


def site_setting_context_processor(request):
    setting = SiteSetting.objects.first()
    return {
        'setting': setting,
    }


def notices_context_processor(request):
    notice_count = NoticeBox.objects.first()
    notices = NoticeBox.objects.all()[:3]
    return {
        'count_notice_header': notice_count,
        'notices_header': notices,
    }
