from django.conf.urls import url

from . import views

app_name = 'photo'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^signup/$', views.SignUpView.as_view(), name='signup'),
]
