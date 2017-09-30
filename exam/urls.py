from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^new$', views.new_exam, name='new≈new_exam'),
    url(r'^create$', views.create, name='create'),
]
