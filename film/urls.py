from django.urls import path
from film.views import IndexView, FilmsView, FilmView, FilmLoginView, RegistrationView, SettingsView, ProfileView, \
    FilmLogoutView

urlpatterns = [
    path(r'', IndexView.as_view(), name='index'),
    path(r'films', FilmsView.as_view(), name='films'),
    path(r'film/<slug>', FilmView.as_view(), name='film'),
    path(r'login', FilmLoginView.as_view(), name='login'),
    path(r'logout', FilmLogoutView.as_view(), name='logout'),
    path(r'registration', RegistrationView.as_view(), name='registration'),
    path(r'settings', SettingsView.as_view(), name='settings'),
    path(r'profile', ProfileView.as_view(), name='profile'),
]
