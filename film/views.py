from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.base import TemplateView, View
from django.views.generic.edit import UpdateView, FormMixin
from film import forms
from film.forms import LoginForm, CreateAccount, SettingsForm
from film.models import Film, User, FavoriteFilms


class IndexView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('films'))
        return super(IndexView, self).get(request, *args, **kwargs)


class FilmsView(LoginRequiredMixin, ListView, FormMixin):
    login_url = reverse_lazy('login')
    model = Film
    paginate_by = 10
    template_name = 'films.html'
    queryset = model.objects.order_by('name')
    form_class = forms.AddFilmForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = forms.AddFilmForm
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            new_film = form.save(commit=True)
            return JsonResponse({
                'href': reverse('film', kwargs={'slug': new_film.slug}),
            })
        return JsonResponse({
            'errors': form.errors,
        }, status=400)


class FilmView(LoginRequiredMixin, DetailView):
    template_name = 'film.html'
    login_url = reverse_lazy('login')
    model = Film

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        film = Film.objects.get(slug=self.kwargs['slug'])
        context['fav'] = FavoriteFilms.objects.filter(uID=self.request.user, fID=film)
        context['user_list'] = FavoriteFilms.objects.filter(fID=film)
        return context


class AddToFavorites(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')

    def post(self, request, slug, *args, **kwargs):
        try:
            FavoriteFilms.objects.get(uID=request.user, fID__slug=slug).delete()
        except FavoriteFilms.DoesNotExist:
            film = Film.objects.get(slug=slug)
            FavoriteFilms.objects.create(uID=request.user, fID=film)

        return HttpResponse(status=200)


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


class ProfileView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['films'] = Film.objects.filter(favoritefilms__uID=self.request.user)
        return context
