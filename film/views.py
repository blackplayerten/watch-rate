from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.base import TemplateView

from film.forms import LoginForm, CreateAccount
from film.models import Film


class IndexView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('films'))
        return super(IndexView, self).get(request, *args, **kwargs)


class FilmsView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')

    model = Film
    paginate_by = 10
    template_name = 'films.html'
    queryset = model.objects.order_by('name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['top_films'] = Film.objects.all().order_by('-user_rating')[:5]
        return context


class FilmView(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('login')

    model = Film
    template_name = 'film.html'


class FilmLoginView(LoginView):
    template_name = 'login.html'
    authentication_form = LoginForm

    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse('films')


class FilmLogoutView(LogoutView):
    def get_next_page(self):
        return reverse('index')


class RegistrationView(CreateView):
    template_name = 'registration.html'
    form_class = CreateAccount

    def get_success_url(self):
        return reverse('index')


class SettingsView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')

    template_name = 'settings.html'


class ProfileView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')

    template_name = 'profile.html'
