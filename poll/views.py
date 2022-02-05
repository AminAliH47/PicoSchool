from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import (
    Http404,
    JsonResponse,
)
from django.shortcuts import (
    render,
    get_object_or_404,
)
from django.urls import reverse_lazy
from django.views import generic
from poll.forms import CreatePollForm
from poll.models import (
    Poll,
    PollOptions,
)


@login_required()
def poll_list(request):
    context = {
        'page_title': 'لیست نظرسنجی ها',
    }
    if request.user.is_superuser or request.user.is_manager:
        context['polls'] = Poll.objects.all()
    elif request.user.is_student:
        context['polls'] = Poll.objects.filter(Q(for_user='student') | Q(for_user='all'))
    elif request.user.is_parent:
        context['polls'] = Poll.objects.filter(Q(for_user='parent') | Q(for_user='all'))
    elif request.user.is_teacher:
        context['polls'] = Poll.objects.filter(Q(for_user='teacher') | Q(for_user='all'))
    return render(request, "poll/poll_list.html", context)


def poll_options_list(request, pk):
    """
    List of Main poll options
    """
    if request.method == "POST" and request.is_ajax:
        poll = get_object_or_404(Poll, pk=pk)
        input_value = {
            'poll': request.POST['poll'],
            'option': request.POST['option'],
        }
        poll.users.clear()
        PollOptions(poll=Poll.objects.get(pk=input_value['poll']), option=input_value['option']).save()
    context = {
        'page_title': 'لیست گزینه ها',
        'options': PollOptions.objects.filter(poll__pk=pk)
    }
    return render(request, "poll/poll_list.html", context)


class PollCreate(LoginRequiredMixin, generic.CreateView):
    form_class = CreatePollForm
    template_name = "poll/poll_create.html"
    success_url = reverse_lazy('poll:poll_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'ساخت نظرسنجی'
        return context


class PollUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Poll
    template_name = "poll/poll_create.html"
    form_class = CreatePollForm
    success_url = reverse_lazy('poll:poll_list')
    context_object_name = "quiz"

    def form_valid(self, form):
        self.obj = form.save(commit=False)
        self.obj.users.clear()
        for option in self.obj.poll_option.all():
            option.option_count = 0
            option.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'ویرایش نظرسنجی'
        return context


@login_required()
def poll_vote(request, pk):
    """
    Vote to main poll options
    """
    poll = get_object_or_404(Poll, pk=pk)
    if request.method == "POST" and request.is_ajax:
        option_id = request.POST['option']
        poll.users.add(request.user)
        option = get_object_or_404(PollOptions, pk=option_id)
        option.option_count += 1
        option.save()
        return JsonResponse({'pk': pk})
    context = {
        'page_title': 'رای به نظرسنجی',
        'poll': poll,
    }
    if poll.active and request.user.pk not in poll.users.values_list('pk', flat=True):
        return render(request, "poll/poll_vote.html", context)
    else:
        raise Http404()


@login_required()
def poll_result(request, pk):
    context = {
        'page_title': 'نتایج نظرسنجی',
        'poll': get_object_or_404(Poll, pk=pk)
    }
    return render(request, "poll/poll_result.html", context)
