from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'detail/(?P<id>\d+)/$', views.game_detail, name='gameplay_detail'),
    url(r'make_move/(?P<id>\d+)/', views.make_move, name="gameplay_make_move"),
    url(r'all$', views.AllGamesList.as_view())
]