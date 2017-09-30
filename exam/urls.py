from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^new$', views.new_exam, name='new_exam'),
    url(r'^create$', views.create, name='create'),
    url(r'^send_email$', views.send_email, name='send_email'),
]
