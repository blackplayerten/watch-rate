from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView
from film.forms import LoginForm, CreateAccount, SettingsForm
from film.models import Film, User


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

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['top_films'] = Film.objects.all().order_by('-user_rating')[:5]
    #     return context


class FilmView(LoginRequiredMixin, DetailView):
    template_name = 'film.html'
    login_url = reverse_lazy('login')
    model = Film


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
        return reverse('profile')


class SettingsView(UpdateView):
    template_name = 'settings.html'
    form_class = SettingsForm
    success_url = 'profile'
    model = User

    def get_object(self, queryset=None):
        return self.request.user

    # def form_valid(self, form):
    #     clean = form.cleaned_data
    #     self.object = form.save(clean)
    #     return super(SettingsView, self).form_valid(form)


class ProfileView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    template_name = 'profile.html'
