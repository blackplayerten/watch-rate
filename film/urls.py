from django.urls import path
from film.views import IndexView, FilmsView, FilmView, FilmLoginView, RegistrationView, SettingsView, ProfileView, \
    FilmLogoutView, AddToFavorites

urlpatterns = [
    path(r'', IndexView.as_view(), name='index'),
    path(r'films', FilmsView.as_view(), name='films'),
    path(r'film/<slug>', FilmView.as_view(), name='film'),
    path(r'film/add_to_fav/<slug>', AddToFavorites.as_view(), name='fav'),
    path(r'login', FilmLoginView.as_view(), name='login'),
    path(r'logout', FilmLogoutView.as_view(), name='logout'),
    path(r'registration', RegistrationView.as_view(), name='registration'),
    path(r'profile', ProfileView.as_view(), name='profile'),
    path(r'settings', SettingsView.as_view(), name='settings'),
]
