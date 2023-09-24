from django.contrib import auth, messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView

from users.models import User
from main.models import Interests
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(username=username, password=password)
            if user:
                print("YEEESSSSS")
                auth.login(request, user)
                return redirect('main_page')
    form = UserLoginForm()
    context = {
        'form': form,
    }
    return render(request, 'users/login.html', context)


def logout(request):
    auth.logout(request)
    return redirect(reverse('main_page'))


class UserRegistrationView(CreateView):
    model = User
    template_name = 'users/registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('users:login')
    success_message = "%(name)s профиль был успешно создан"


class UserProfileView(UpdateView):
    model = User
    template_name = 'users/profile.html'
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')
    success_message = "%(name)s профиль был успешно обновлен"

    def get_success_url(self):
        return reverse_lazy('users:profile', args=[self.object.id])

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data()
        context['infos'] = User.objects.filter(username=self.object)
        return context
