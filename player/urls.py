from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView

from . import views

urlpatterns = [
    url(r'home$', views.home, name="player_home"),
    url(r'^$', views.index, name="player_index"),
    url(r'login$', LoginView.as_view(template_name="player/login_form.html"), name="player_login"),
    url(r'logout$', LogoutView.as_view(), name="player_logout"),
    url(r'new_invitation$', views.new_invitation, name="player_new_invitation"),
    url(r'accept_invitation/(?P<id>\d+)$', views.accept_invitation, name="player_accept_invitation"),
    url(r'signup$', views.SignUpView.as_view(), name='player_signup'),
]