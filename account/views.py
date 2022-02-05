from django.contrib import (
    auth,
    messages,
)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import (
    render,
    redirect,
)
from django.urls import reverse_lazy
from account.decorators import is_login
from account.models import User


@is_login()
def login_view(request):
    if request.method == 'POST':
        user_input = request.POST['username']
        try:
            username = User.objects.get(national_code=user_input).username
        except User.DoesNotExist:
            username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'نام کاربری یا گذرواژه وارد شده نادرست است')
    context = {
        'page_title': 'ورود',
    }
    return render(request, "account/signin.html", context)


class ChangePasswordView(PasswordChangeView):
    template_name = "manager/persons/change_password.html"
    success_url = reverse_lazy('account:user_password_done')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "تغییر گذرواژه"
        return context


@login_required()
def password_change_done(request):
    return render(request, "manager/persons/change_password_done.html", {"page_title": "گذرواژه با موفقیت تغییر کرد"})
