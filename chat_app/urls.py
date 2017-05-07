from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^home$', views.home, name='home'),
    url(r'^signup$', views.signup, name='signup'),
    url(r'^login/$', auth_views.login, {'template_name': 'chat_app/login.html'},name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
]