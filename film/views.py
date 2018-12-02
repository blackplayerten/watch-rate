from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
from film.models import Film


class IndexView(TemplateView):
    template_name = 'index.html'


class FilmsView(ListView):
    model = Film
    paginate_by = 10
    template_name = 'films.html'
    queryset = model.objects.order_by('name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['top_films'] = Film.objects.all().order_by('-user_rating')[:5]
        return context


class FilmView(DetailView):
    model = Film
    template_name = 'film.html'


class LoginView(TemplateView):
    template_name = 'login.html'


class RegistrationView(TemplateView):
    template_name = 'registration.html'


class SettingsView(TemplateView):
    template_name = 'settings.html'


class ProfileView(TemplateView):
    template_name = 'profile.html'
